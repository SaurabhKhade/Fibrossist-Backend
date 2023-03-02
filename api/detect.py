from flask import request
from models.providers.validateXRay import validateXRay
from models.providers.detectFibrosis import detectFibrosis
from functions.crypto import decrypt, hash
from functions.save_history import save_history

import os
import time


def detect():
    id = request.headers.get('token')
    if not id:
        return {"status": 400, "message": "id not provided"}, 400

    id = decrypt(id, str(request.remote_addr))
    dir_path = os.path.join('static', 'users', hash(id), 'uploads')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    img_path = os.path.join(dir_path, f'{time.time()}.png')

    try:
        if "image" not in request.files:
            return {'status': 400, 'message': 'No image found! make sure it has name as \'image\''}, 400
        file = request.files['image']
        file.save(img_path)

        isValid = validateXRay(img_path)
        if not isValid:
            os.remove(img_path)
            return {'status': 400, 'message': 'The provided X-Ray image appears to be invalid! Please check the image and try again.'}, 400

        isNormal = detectFibrosis(img_path)
        # print(isNormal)
        history_id = save_history(id, isNormal, img_path)
        # print(history_id)

        if (isNormal):
            return {'status': 200, 'message': 'Success', 'data': 'No Fibrosis Detected', 'history': history_id}, 200
        else:
            return {'status': 200, 'message': 'Success', 'data': 'Fibrosis Detected', 'history': history_id}, 200

    except Exception as e:
        print(e)
        return {'status': 500, 'message': 'Internal Server Error'}, 500
