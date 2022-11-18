from flask import request, abort
from functions.crypto import encrypt, hash
from functions.validation import invalid_signup
from database.db import db
import json

def signup():
    if request.method == 'GET':
        return {"status": 400, "message": "Expected request structure", 
                "data": {
                    "email": "string",
                    "password": "string",
                    "name": "string",
                    "surname": "string",
                    "age": "number",
                    "gender": "string (M, F or O)"
                }}, 400
    try:
        data = request.data
        
        # handling invalid data 
        if len(data) == 0:
            return {"status": 400, "message": "No data provided"}, 400

        data = json.loads(data.decode('utf-8'))
        users = db["auth"]

        if invalid_signup(data):
            return {"status": 400, "message": invalid_signup(data)}, 400

        # if user already exists, convey so, if not create user
        user = users.find_one({"email": data["email"]})

        if user:
            return {"status": 409, "message": "User with this email already exists"}, 409
        else:
            
            password = hash(data["password"])
            user = users.insert_one({"email": data["email"], "password": password})
            details = users = db["users"]
            details.insert_one({ "_id": user.inserted_id, "name": data["name"], 
                                "surname": data["surname"], "age": data["age"], 
                                "email": data["email"], "gender": data["gender"]})
            return {"status": 200, "message": "Sign up successful", "token": encrypt(str(user.inserted_id),str(request.remote_addr))}, 200
    
    except Exception as e:
        print(e)
        abort(500)