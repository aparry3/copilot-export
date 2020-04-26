import os
import pymongo

client = pymongo.MongoClient(os.getenv('MONGO_DEV_URI'))
db = client.copilot
