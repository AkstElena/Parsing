from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.steam


def find():
    query = {"developer": "CD PROJEKT RED"}

    games = db.games.find(query)
    for a in games:
        print(a)


if __name__ == '__main__':
    find()
