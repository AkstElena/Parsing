from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')

db = client.steam

def find():
    #query = {"positive" : {"$gt" : 500000, "$lte" : 600000}}
    #query = {"name" : {"$gte" : "A", "$lt" : "D"}}
    #query = {"required_age" : {"$ne" : 0}}
    #query = {"tags" : {"$exists" : 1}}
    #query = {"name" : {"$regex" : "[Pp]uzzle"}}
    #query = {"name" : {"$regex" : "[Pp]uzzle | [Gg]ame"}}
    #query = {"categories" : "Co-op"}
    #query = {"categories" : {"$in" : ["Co-op", "Online PvP"]}}
    query = {"categories" : {"$all" : ["Co-op", "Remote Play on Tablet", "Steam Achievements"]}}
    #query = {"categories" : {"$all" : ["Steam Trading Cards", "Co-op", "Remote Play on Tablet", "Steam Achievements"]}}
    #query = {"type" : {"$ne" : "game"}}


    projection = {"_id" : 0, "name" : 1}

    games = db.games.find(query, projection)
    
    num_games = 0
    for i in games:
        print(i)
        num_games += 1
        
    print('Число игр: %d' % num_games)

    for a in games:
        print(a)
        
if __name__ == '__main__':
    find()