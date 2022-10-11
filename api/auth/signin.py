from functions.crypto import encrypt
from database.db import db
from flask import request
from hashlib import sha256
import json

def signin():
    data = request.data
    data = json.loads(data.decode('utf-8'))
    users = db["users"]
    user = users.find_one({"email": data["email"]})
    if user:
        password = sha256(data["password"].encode('utf-8')).hexdigest()
        if user["password"] == password:
            return {"status": 200, "message": "Sign in successful", "token": encrypt(str(user["_id"]))}, 200
        else:
            return {"status": 401, "message": "Incorrect password"}, 401
    else:
        return {"status": 404, "message": "User not found"}, 404
      
