from pymongo import MongoClient

user = input('Enter username: ')
password = input('Enter password: ')

# create database connection
cluster = MongoClient(
    f'mongodb+srv://{user}:{password}@fibrossistcluster.jj87sms.mongodb.net/?retryWrites=true&w=majority'
)

db = cluster["FibrossistCluster"]

print("[1] Deleting all documents from 'auth' collection")
db['auth'].delete_many({})
print("Done.")
print("[2] Deleting all documents from 'users' collection")
db['users'].delete_many({})
print("Done.")
print("[3] Deleting all documents from 'contact' collection")
db['contact'].delete_many({})
print("Done.")
print("[4] Deleting all documents from 'history' collection")
db['history'].delete_many({})
print("Done.")
print("[5] Deleting all documents from 'otp' collection")
db['otp'].delete_many({})
print("Done.")
print("[6] Deleting all documents from 'stats' collection")
db['stats'].delete_many({})
print("Done.")
