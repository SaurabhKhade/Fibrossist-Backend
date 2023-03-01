from flask import request
from .crypto import decrypt, hash
from database import db
from bson.objectid import ObjectId
import datetime


def save_history(id, isNormal):
    stats = db['stats']

    if stats.find_one({'id': ObjectId(id)}):
        if isNormal:
            stats.update_one({'id': ObjectId(id)}, {'$inc': {'negative': 1}})
        else:
            stats.update_one({'id': ObjectId(id)}, {'$inc': {'positive': 1}})
    else:
        if isNormal:
            stats.insert_one(
                {'id': ObjectId(id), 'negative': 1, 'positive': 0})
        else:
            stats.insert_one(
                {'id': ObjectId(id), 'negative': 0, 'positive': 1})

    db.history.insert_one({'user_id': id, 'isNormal': isNormal, 'date': datetime.date.today().strftime('%d-%m-%Y'),
                           "time": datetime.datetime.now().time().strftime('%H:%M:%S')})

    # data,time,result,age
