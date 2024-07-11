"""
Работа с https://api.kinopoisk.dev
"""

import requests
import pandas as pd
import json

name = input("Введите название фильма: ")

# endpoint = "https://api.kinopoisk.dev/v1.4/movie/random"
endpoint = "https://api.kinopoisk.dev/v1.4/movie/search"

headers = {"accept": "application/json", "X-API-KEY": "1C6EWNM-VY8ME6Y-MSCD6PE-W2JETDZ", }
params = {
    "query": name,

}
response = requests.get(endpoint, params=params, headers=headers)
# response = requests.get(endpoint, headers=headers)
print(response.text)

with open('hw_1_kinopoisk.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)

if response.status_code == 200:
    print("Успешный запрос")
    data = response.json()
    movies = data["docs"]
    print(data)

    movies_data = []
    #     for movie in movies:
    #         name = movie.get("name", "-")
    #         rating = movie.get("location", {}).get("kp", "-")
    #         description = movie.get("description", "-")
    #         year = movie.get("year", "-")
    #         movies_data.append({"Название": name, 'Рейтинг': rating, 'Год выхода': year, 'Описание': description})
    #     df = pd.DataFrame(movies_data)
    #     print(df.head)
    # else:
    #     print("Запрос не удался", response.status_code)

    for movie in movies:
        name = movie.get("name", "-")
        rating = movie.get("rating", {}).get("kp", "-")
        description = movie.get("description", "-")
        year = movie.get("year", "-")
        movie_dict = {"Название": name, 'Рейтинг': rating, 'Год выхода': year, 'Описание': description}
        movies_data.append(movie_dict)
else:
    print("Запрос не удался", response.status_code)

with open('hw_1_movies.json', 'w', encoding='utf-8') as f:
    json.dump(movies_data, f, ensure_ascii=False, indent=4)
    print('file created')
