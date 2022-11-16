from pymongo import MongoClient

# create database connection 
cluster = MongoClient(
        f'mongodb+srv://SaurabhKhade:SaurabhKhade@fibrossistcluster.jj87sms.mongodb.net/?retryWrites=true&w=majority'
    )

db = cluster["FibrossistCluster"]

db.auth.create_index([("email", 1)], unique=True)
db.users.create_index([("email", 1),("user_id",1)], unique=True)