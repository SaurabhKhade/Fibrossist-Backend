from flask import request, abort
from functions.crypto import encrypt, hash
from database.db import db
import json

def invalid(data):
    if "email" not in data:
        return "Email is required"
    elif "password" not in data:
        return "Password is required"
    elif "name" not in data:
        return "Name is required"
    elif "surname" not in data:
        return "Surname is required"
    elif "age" not in data:
        return "Age is required"
    else:
        return False

def signup():
    try:
        data = request.data
        if len(data) == 0:
            return {"status": 400, "message": "No data provided"}, 400

        data = json.loads(data.decode('utf-8'))
        users = db["users"]

        if invalid(data):
            return {"status": 400, "message": invalid(data)}, 400
        user = users.find_one({"email": data["email"]})

        if user:
            return {"status": 409, "message": "User with this email already exists"}, 409
        else:
            password = hash(data["password"])
            user = users.insert_one({"email": data["email"], "password": password})
            return {"status": 200, "message": "Sign up successful", "token": encrypt(str(user.inserted_id))}, 200
    
    except Exception as e:
        print("Error",e)
        abort(500)