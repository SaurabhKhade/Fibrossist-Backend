from flask import request
from models.providers.validate import validate
import os

def detect():
    if "image" not in request.files:
        return {'status': 400, 'message': 'No image found'}, 400
    file = request.files['image']
    path = os.path.join('uploads', file.filename)
    file.save(path)
    result = validate(path)
    os.remove(path)
    if(result):
        return {'status': 200, 'message': 'Valid X-Ray image'}, 200
    else:
        return {'status': 400, 'message': 'Invalid X-Ray image'}, 400
