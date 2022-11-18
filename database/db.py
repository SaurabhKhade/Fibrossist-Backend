# import os
from pymongo import MongoClient

# print(os.environ.get("DB_USER"))

# create database connection 
cluster = MongoClient(
        f'mongodb+srv://SaurabhKhade:SaurabhKhade@fibrossistcluster.jj87sms.mongodb.net/?retryWrites=true&w=majority'
    )

db = cluster["FibrossistCluster"]
