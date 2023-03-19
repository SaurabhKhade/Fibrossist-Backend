from flask import abort, request, send_from_directory
from functions.crypto import decrypt
from database.db import db
import json


def verify(creds):
    if request.method == 'OPTIONS':
        return {"status": 200, "message": "OK"}, 200
    try:
        data = json.loads(decrypt(creds, ''))
        otp = db["otp"]
        saved_otp = otp.find_one({"email": data["email"]})
        if saved_otp:
            if saved_otp["otp"] == data["otp"]:
                users = db["auth"]
                details = db["users"]
                saved_data = json.loads(saved_otp["data"])
                user = users.insert_one(
                    {"email": saved_data["email"], "password": saved_data["password"]})
                details.insert_one({"_id": user.inserted_id, "name": saved_data["name"],
                                    "surname": saved_data["surname"], "birthDate": saved_data["birthDate"],
                                    "email": saved_data["email"], "gender": saved_data["gender"]})
                otp.delete_one({"email": data["email"]})
                return send_from_directory('static', 'email_verified.html')
            else:
                return '<h1 style="text-align: center;margin-top: 100px;">Invalid OTP</h1>', 400
        else:
            return '<h1 style="text-align: center;margin-top: 100px;">Invalid OTP</h1>', 400

    except Exception as e:
        print(e)
        abort(500)
