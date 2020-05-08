import os
import pymongo
from config import app

client = pymongo.MongoClient(app.config.get('MONGO_URI'))
db = client.copilot
