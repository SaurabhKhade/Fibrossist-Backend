from flask import request, abort
from functions.crypto import encrypt, hash
from database.db import db
import json

def signup():
    try:
        data = request.data
        data = json.loads(data.decode('utf-8'))
        users = db["users"]
        user = users.find_one({"email": data["email"]})
        if user:
            return {"status": 409, "message": "User with this email already exists"}, 409
        else:
            password = hash(data["password"])
            user = users.insert_one({"email": data["email"], "password": password})
            return {"status": 200, "message": "Sign up successful", "token": encrypt(str(user.inserted_id))}, 200
    except:
        abort(500)