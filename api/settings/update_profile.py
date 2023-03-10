from flask import request
import os
from functions.crypto import hash, decrypt


def updateProfile():
    if request.method == 'OPTIONS':
        return {'status': 200, 'message': 'Success'}, 200

    id = request.headers.get('token')
    id = decrypt(id, str(request.remote_addr))
    if not id:
        return {"status": 400, "message": "id not provided"}, 400

    dir_path = os.path.join('static', 'users', hash(id), 'profile')
    # print(dir_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    img_path = os.path.join(dir_path, 'profile.png')

    try:
        if "profile" not in request.files:
            return {'status': 400, 'message': 'No image found! make sure it has name as \'image\''}, 400
        file = request.files['profile']

        file.save(img_path)

        return {'status': 200, 'message': 'Success', 'data': {'path': img_path}}, 200
    except:
        return {'status': 500, 'message': 'Internal Server Error'}, 500
