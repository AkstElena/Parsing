import requests
import pandas as pd

# Ваши учетные данные API
client_id = "__"
client_secret = "__"

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"
city = input("Введите название города: ")
place = input("Введите тип заведения: ")
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": place,
}
headers = {
    "Accept": "application/json",
    "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI=",
}

response = requests.get(endpoint, params=params, headers=headers)
if response.status_code == 200:
    print("Успешный запрос")
    data = response.json()  # Directly use .json() method
    venues = data["results"]

    venues_data = []
    for venue in venues:
        name = venue["name"]
        address = venue.get("location", {}).get("address", "Адрес не указан")

        venues_data.append({"Название": name, "Адрес": address})

    df = pd.DataFrame(venues_data)
    print(df.head)
else:
    print("Запрос не удался", response.status_code)
