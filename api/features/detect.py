from flask import request
from models.providers.validateXRay import validateXRay
from models.providers.detectFibrosis import detectFibrosis
from functions.crypto import decrypt, hash

import os
import time


def detect():
    try:
        if "image" not in request.files:
            return {'status': 400, 'message': 'No image found'}, 400
        file = request.files['image']
        id = request.headers.get('token')
        if not id:
            return {"status": 400, "message": "id not provided"}, 400

        id = decrypt(id, str(request.remote_addr))
        dir_path = os.path.join('static', 'users', hash(id), 'uploads')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        img_path = os.path.join(dir_path, f'{time.time()}.png')
        # img_path = 'uploads/img_file_for_detection.{}'.format(file.filename.split('.')[-1])
        file.save(img_path)
        # print(img_path)
        isValid = validateXRay(img_path)
        if not isValid:
            return {'status': 400, 'message': 'The provided X-Ray image appears to be invalid!'}, 400
        isNormal = detectFibrosis(img_path)

        # os.remove(img_path)
        if (isNormal):
            return {'status': 200, 'message': 'Success', 'data': 'No Fibrosis Detected'}, 200
        else:
            return {'status': 200, 'message': 'Success', 'data': 'We think you might have fibrosis, please talk with your doctor immediately'}, 200
    except Exception as e:
        print(e)
        return {'status': 500, 'message': 'Internal Server Error'}, 500
