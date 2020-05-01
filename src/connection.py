import os
import pymongo

print(os.getenv('MONGO_DEV_URI'))
client = pymongo.MongoClient(os.getenv('MONGO_DEV_URI'))
db = client.copilot
