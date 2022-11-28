import os
from pymongo import MongoClient

# create database connection 
cluster = MongoClient(
        f'mongodb+srv://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASS")}@fibrossistcluster.jj87sms.mongodb.net/?retryWrites=true&w=majority'
    )

db = cluster["FibrossistCluster"]
