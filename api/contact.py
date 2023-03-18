from flask import request
from functions.crypto import decrypt
from database.db import db


def contact():
    try:
        if request.method == 'OPTIONS':
            return {"status": 200, "message": "OK"}, 200

        id = request.headers.get('token')
        if not id:
            return {"status": 400, "message": "id not provided"}, 400

        id = decrypt(id, str(request.remote_addr))

        data = request.get_json()
        # print(request_data['name'])

        contacts = db["contact"]
        contacts.insert_one(data)

        return "OK", 200

    except Exception as e:
        print(e)
        return {"status": 500, "message": "Internal Server Error"}, 500
