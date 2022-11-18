from flask import request
from models.providers.validateXRay import validateXRay
from models.providers.detectFibrosis import detectFibrosis
import os

def detect():
    if "image" not in request.files:
        return {'status': 400, 'message': 'No image found'}, 400
    file = request.files['image']
    img_path = 'uploads/img_file_for_detection.{}'.format(file.filename.split('.')[-1])
    file.save(img_path)
    # print(img_path)
    isValid = validateXRay(img_path)
    if not isValid:
        return {'status': 400, 'message': 'The provided X-Ray image appears to be invalid!'}, 400
    hasFibrosis = detectFibrosis(img_path)
    os.remove(img_path)
    if(hasFibrosis):
        return {'status': 200, 'message': 'Success', 'data': 'We think you might have fibrosis, please talk with your doctor immediately'}, 200
    else:
        return {'status': 200, 'message': 'Success', 'data': 'No Fibrosis Detected'}, 200
