"""
Домашнее задание
1. Ознакомиться с некоторые интересными API.
https://docs.ozon.ru/api/seller/
https://developers.google.com/youtube/v3/getting-started
https://spoonacular.com/food-api

2. Потренируйтесь делать запросы к API. 
Выберите публичный API, который вас интересует, и потренируйтесь делать API-запросы с помощью Postman.
Поэкспериментируйте с различными типами запросов и попробуйте получить различные типы данных.

3. Сценарий Foursquare
- Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию
(например, кофейни, музеи, парки и т.д.).
- Используйте API Foursquare для поиска заведений в указанной категории.
- Получите название заведения, его адрес и рейтинг для каждого из них.
- Скрипт должен вывести название и адрес и рейтинг  каждого заведения в консоль.
"""


import requests
# import pandas as pd
#
# # Ваши учетные данные API
# client_id = "__"
# client_secret = "__"
#
# # Конечная точка API
# endpoint = "https://api.foursquare.com/v3/places/search"
# city = input("Введите название города: ")
# place = input("Введите тип заведения: ")
# params = {
#     "client_id": client_id,
#     "client_secret": client_secret,
#     "near": city,
#     "query": place,
# }
# headers = {
#     "Accept": "application/json",
#     "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI=",
# }
#
# response = requests.get(endpoint, params=params, headers=headers)
# if response.status_code == 200:
#     print("Успешный запрос")
#     data = response.json()  # Directly use .json() method
#     venues = data["results"]
#
#     venues_data = []
#     for venue in venues:
#         name = venue["name"]
#         address = venue.get("location", {}).get("address", "Адрес не указан")
#
#         venues_data.append({"Название": name, "Адрес": address})
#
#     df = pd.DataFrame(venues_data)
#     print(df.head)
# else:
#     print("Запрос не удался", response.status_code)

# import requests
#
# url = "https://api.foursquare.com/v3/places/search"
#
# client_id = "VXXLBMEYF3R2IYNBIDGQBVQIO1WDML5KDUXXCUPUDPRL0HX0"
# client_secret = "F1UD0TCIIIQCBU3UIDMLBHV55LFZG13WMGO5QOL0D03ALJN0"
# headers = {"accept": "application/json", "Authorization": "fsq3px5gZIImsYoeEsJkCjfNEtsOizurkjE+gLXlX31zcSc=",}
# params = {
#     "client_id": client_id,
#     "client_secret": client_secret,
# }
# response = requests.get(url, params=params, headers=headers)
#
# print(response.text)