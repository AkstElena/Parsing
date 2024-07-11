from bs4 import BeautifulSoup
import urllib.parse
import requests
import re
import json



import requests

url = "https://api.foursquare.com/v3/places/650c5860b8e63514a2aa5aa6"

headers = {
    "accept": "application/json",
    "Authorization": "fsq3aMuRcI4J0fXOiJuYYjlJYTkzdOznt8tfr1/qOS3PH6I=",
    "fsq_id": "650c5860b8e63514a2aa5aa6",
}

response = requests.get(url, headers=headers)

print(response.text)

with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)


endpoint = "https://api.foursquare.com/v3/places/search"

client_id = "__"
client_secret = "__"
# Определение параметров для запроса API
# city = input("Введите название города: ")
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": 'New York',
    "query": "restaurant",
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI=",
}


response = requests.get(endpoint, params=params, headers=headers)

# Проверка успешности запроса API

with open('test2.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)