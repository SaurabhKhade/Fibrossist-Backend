from flask import request
from functions.crypto import decrypt
from database.db import db
from bson import ObjectId


def updateDetails():
    if request.method == 'OPTIONS':
        return {'status': 200, 'message': 'Success'}, 200

    id = request.headers.get('token')
    if not id:
        return {"status": 400, "message": "id not provided"}, 400
    id = decrypt(id, str(request.remote_addr))

    try:
        users = db["users"]
        data = request.get_json()
        # return print(data)
        users.update_one({"_id": ObjectId(id)}, {"$set": data})
        return {"status": 200, "message": "Success"}, 200
    except Exception as e:
        print(e)
        return {"status": 500, "message": "Internal Server Error"}, 500
