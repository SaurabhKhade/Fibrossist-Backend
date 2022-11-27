from flask import abort
from functions.crypto import decrypt,hash
from database.db import db
import json

def verify(creds):
    try:
        data = json.loads(decrypt(creds,''))
        otp = db["otp"]
        saved_otp = otp.find_one({"email": data["email"]})
        if saved_otp:
            if saved_otp["otp"] == data["otp"]:
                users = db["auth"]
                details = db["users"]
                saved_data = json.loads(saved_otp["data"])
                password = hash(saved_data["password"])
                user = users.insert_one({"email": saved_data["email"], "password": password})
                details.insert_one({ "_id": user.inserted_id, "name": saved_data["name"], 
                                    "surname": saved_data["surname"], "age": saved_data["age"], 
                                    "email": saved_data["email"], "gender": saved_data["gender"]})
                otp.delete_one({"email": data["email"]})
                return {"status": 200, "message": "Email verified successfully."}, 200
            else:
                return {"status": 400, "message": "Invalid OTP"}, 400
        else:
            return {"status": 400, "message": "Invalid OTP"}, 400

    except Exception as e:
        print(e)
        abort(500)