from flask import request, abort
from functions.crypto import encrypt, hash
from functions.validation import invalid_signup
from database.db import db
import json

def signup():
    try:
        data = request.data
        
        # handling invalid data 
        if len(data) == 0:
            return {"status": 400, "message": "No data provided"}, 400

        data = json.loads(data.decode('utf-8'))
        users = db["users"]

        if invalid_signup(data):
            return {"status": 400, "message": invalid_signup(data)}, 400

        # if user already exists, convey so, if not create user
        user = users.find_one({"email": data["email"]})

        if user:
            return {"status": 409, "message": "User with this email already exists"}, 409
        else:
            password = hash(data["password"])
            user = users.insert_one({"email": data["email"], "password": password})
            return {"status": 200, "message": "Sign up successful", "token": encrypt(str(user.inserted_id))}, 200
    
    except Exception as e:
        print(e)
        abort(500)