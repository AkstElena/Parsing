from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client.steam


def find():
    sysreq = ["Win 10 64-bit version",
              "Intel Core i5-3570 @3.4 GHz or AMD Ryzen 3 1300X @3.5 GHz",
              "NVIDIA GeForce GTX 650 TI (2GB) or AMD HD 7750 (1GB)",
              "8GB System RAM",
              "Minimum 2GB free space on hard drive (additional space required for add-on downloads)",
              "High speed broadband connection required for online play"]

    db.games.update_one({"name": "Quake"},
                        {"$set": {"sysreq": sysreq}}
                        )

    #    db.games.update_many ({},
    #                        {"$set" : {"sysreq" : "No requirements"}}
    #                        )

    query = {"name": "Quake"}
    projection = {"_id": 0, "name": 1, "sysreq": 1}
    game = db.games.find_one(query, projection)

    print(game)


if __name__ == '__main__':
    find()
