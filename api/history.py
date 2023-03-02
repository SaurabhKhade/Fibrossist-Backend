from flask import request
from database.db import db
from bson import ObjectId
from functions.crypto import decrypt
from datetime import datetime


def history():
    id = request.args.get('id')
    if not id:
        return returnAll()
    item = db['history'].find_one({'_id': ObjectId(id)}, {"_id": 0})
    return item


def returnAll():
    token = request.headers.get('token')
    if not token:
        return {"status": 400, "message": "Token not provided"}, 400
    id = decrypt(token, str(request.remote_addr))
    print(id)
    items = db['history'].find({'user_id': id}, {"_id": 0})
    return sorted(list(items), key=sort_key, reverse=True)


def sort_key(sublist):
    date_str, time_str = sublist['date'], sublist['time']
    return datetime.strptime(date_str, '%d-%m-%Y'), datetime.strptime(time_str, '%H:%M:%S')
