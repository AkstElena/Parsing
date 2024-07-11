# импорт модуля
from pymongo import MongoClient

# создание нового объекта MongoClient для подключения к локальному серверу MongoDB
client = MongoClient('mongodb://localhost:27017')

# создание словаря Python с информацией об игре
witcher = {
    "appid": 292030,
    "positive": 632627,
    "negative": 25245,

    "name": "The Witcher 3: Wild Hunt",
    "developer": "CD PROJEKT RED",
    "publisher": "CD PROJEKT RED",
    "genre": "RPG",
    "release_date": "2015/05/18",

    "tags": {
        "Open World": 11677,
        "RPG": 10024,
        "Story Rich": 9219,
        "Atmospheric": 6478,
        "Mature": 6234,
        "Fantasy": 6057
    }
}

# подключение к базе данных "steam" на сервере MongoDB
db = client.steam
# добавление данных в коллекцию "games" в базе данных "steam"
db.games.insert_one(witcher)

# найти все документы в коллекции "games" и вывести их на консоль
for a in db.games.find():
    print(a)
