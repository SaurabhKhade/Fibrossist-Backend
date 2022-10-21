from functions.crypto import encrypt, hash
from database.db import db
from flask import request, abort
import json

def signin():
    try:
        data = request.data

        # handling invalid data 
        if len(data) == 0:
            return {"status": 400, "message": "No data provided"}, 400
        data = json.loads(data.decode('utf-8'))
        users = db["users"]
        if "email" not in data:
            return {"status": 400, "message": "Email is required"}, 400
        elif "password" not in data:
            return {"status": 400, "message": "Password is required"}, 400

        # if user exists verify password, if not convey so 
        user = users.find_one({"email": data["email"]})
        if user:
            password = hash(data["password"])
            if user["password"] == password:
                return {"status": 200, "message": "Signed in successfully", "token": encrypt(str(user["_id"]), str(request.remote_addr))}, 200
            else:
                return {"status": 401, "message": "Incorrect password"}, 401
        else:
            return {"status": 404, "message": "User not found"}, 404
    except:
        abort(500)
