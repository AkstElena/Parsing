"""
Задание 3

- Создайте сценарий Python, который запрашивает данные из Foursquare API с помощью библиотеки requests.
- Сценарий должен предложить пользователю ввести название города.
- Затем сценарий должен отправить запрос в Foursquare API для поиска ресторанов в указанном городе.
- Сценарий должен обработать ответ API и извлечь название и адрес каждого ресторана.
- Скрипт должен вывести название и адрес каждого ресторана в консоль.

Требования:
Использовать API Foursquare для получения данных.
Использовать библиотеку requests для отправки запросов API
Использовать библиотеку json для обработки ответа API.
Запросить у пользователя название города
Извлечь и вывести название и адрес каждого ресторана из ответа API.
Работа с API для сбора и обработки данных, а затем создание DataFrame для подготовки данных к анализу.

- Перенести код из блока 3 в Google Colab.
- Модифицировать код, чтобы извлечь адрес, название ресторана, а также координаты (долгота и широта)
- Создать pandas DataFrame из полученных данных
"""

import requests
import json

# Ваши учетные данные API
client_id = "__"
client_secret = "__"

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"


# Определение параметров для запроса API
city = input("Введите название города: ")
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": "restaurant",
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI=",
}


response = requests.get(endpoint, params=params, headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text)  # Парсим JSON-ответ в словарь Python
    venues = data["results"]  # Получаем список мест из данных ответа
    for venue in venues:  # Проходимся по каждому месту в списке
        print("Название:", venue["name"])
        try:
            print("Адрес:", venue["location"]["address"])
        except Exception:
            print("Адрес отсутствует!")
        print("\n")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)
