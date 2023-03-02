from flask import request
from bson import ObjectId
from database.db import db
from functions.crypto import decrypt, hash
from os import path
import datetime


def details():
    try:
        if request.method == 'OPTIONS':
            return {"status": 200, "message": "OK"}, 200

        id = request.headers.get('token')
        if not id:
            return {"status": 400, "message": "id not provided"}, 400

        id = decrypt(id, str(request.remote_addr))

        users = db["users"]
        user = users.find_one(
            {'_id': ObjectId(id)}, {"_id": 0})
        if not user:
            return {"status": 404, "message": "User not found"}, 404

        user['age'] = (datetime.datetime.now(
        )-datetime.datetime.strptime(user['birthDate'], '%d-%m-%Y')).days//365

        stats = db["stats"]
        stat = stats.find_one(
            {'_id': ObjectId(id)}, {"_id": 0})
        print(stat)
        if not stat:
            stat = {
                "negative": 0,
                "positive": 0,
            }

        if path.exists(f"static/profile/{hash(id)}/profile.jpg"):
            profile = {
                "exists": True,
                "path": f"static/profile/{hash(id)}/profile.jpg"
            }
        else:
            profile = {
                "exists": False
            }

        data = {
            "details": user,
            "stats": stat,
            "profile": profile
        }
        return data, 200
    except Exception as e:
        return {"status": 500, "message": "Internal Server Error"}, 500
