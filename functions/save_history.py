from database.db import db
from bson.objectid import ObjectId
import datetime
# import os


def save_history(id, isNormal, img_path):
    stats = db['stats']

    if stats.find_one({'_id': ObjectId(id)}):
        if isNormal:
            stats.update_one({'_id': ObjectId(id)}, {
                             '$inc': {'negative': 1}})
        else:
            stats.update_one({'_id': ObjectId(id)}, {
                             '$inc': {'positive': 1}})
    else:
        if isNormal:
            stats.insert_one(
                {'_id': ObjectId(id), 'negative': 1, 'positive': 0})
        else:
            stats.insert_one(
                {'_id': ObjectId(id), 'negative': 0, 'positive': 1})

    user = db['users'].find_one({'_id': ObjectId(id)})
    age = (datetime.datetime.now(
    )-datetime.datetime.strptime(user['birthDate'], '%d-%m-%Y')).days//365

    history = db.history.insert_one({'user_id': id, 'isNormal': isNormal, 'date': datetime.date.today().strftime('%d-%m-%Y'),
                                    "time": datetime.datetime.now().time().strftime('%H:%M:%S'), 'age': age, 'img_path': img_path})
    return str(history.inserted_id)
