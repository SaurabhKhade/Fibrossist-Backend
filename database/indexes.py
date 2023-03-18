from pymongo import MongoClient

user = input('Enter username: ')
password = input('Enter password: ')

# create database connection
cluster = MongoClient(
    f'mongodb+srv://{user}:{password}@fibrossistcluster.jj87sms.mongodb.net/?retryWrites=true&w=majority'
)

db = cluster["FibrossistCluster"]

db.auth.create_index([("email", 1)], unique=True)
db.users.create_index([("email", 1), ("user_id", 1)], unique=True)
db.otp.create_index([("email", 1)], unique=True)
db.otp.create_index([("createdAt", 1)], expireAfterSeconds=600)
