import os
from pymongo import MongoClient

cluster = MongoClient(
        f'mongodb+srv://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASS")}@fibrossistcluster.1mfgosz.mongodb.net/?retryWrites=true&w=majority'
    )

db = cluster["Fibrossist"]
