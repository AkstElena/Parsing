# импорт модуля
from pymongo import MongoClient

# создание нового объекта MongoClient для подключения к локальному серверу MongoDB
client = MongoClient('mongodb://localhost:27017')

# подключение к базе данных "steam" на сервере MongoDB
db = client.steam


# определение функции, которая находит и выводит игры, соответствующие определенному запросу и проекции
def find():
    # определение запроса для поиска игр с разработчиком "Valve" и жанром "Action"
    query = {"developer": "CD PROJEKT RED",
             "genre": "RPG"}

    # определение проекции для исключения поля "_id" и включения только поля "name"
    projection = {"_id": 0, "name": 1}
    # поиск игр, соответствующих запросу и проекции
    games = db.games.find(query, projection)

    # вывод каждой игры в консоль
    for a in games:
        print(a)


# выполнение функции "find" при запуске скрипта
if __name__ == '__main__':
    find()
