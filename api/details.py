from flask import request
from bson.objectid import ObjectId
from database.db import db
from functions.crypto import decrypt, hash
from os import path


def details():
    try:
        if request.method == 'OPTIONS':
            return {"status": 200, "message": "OK"}, 200

        # print(request.headers)

        id = decrypt(request.headers.get('token'), str(request.remote_addr))
        if not id:
            return {"status": 400, "message": "id not provided"}, 400
        # print(ObjectId(id))
        id = ObjectId(id)
        # print(id)
        # print(type(id))

        users = db["users"]
        user = users.find_one(id)
        if not user:
            return {"status": 404, "message": "User not found"}, 404

        stats = db["stats"]
        stat = stats.find_one(id)
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
        print(e)
        return {"status": 500, "message": "Internal server error"}, 500
