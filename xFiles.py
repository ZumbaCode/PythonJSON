import pymongo
import json

with open("bot.json", "r") as rf:
    decode_data = json.load(rf)

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['dbBot']

col = db['Bot']

col.insert_one(decode_data)