from api.home import home
from api.auth.signup import signup
from api.auth.signin import signin
# from api.features.validate import validate
from api.detect import detect
# from models.providers.functions.ResNet34 import Resnet34 as ResNet34
from api.auth.verify import verify
from api.auth.recover import send_otp, verify_otp
from api.details import details
from api.history import history

from flask import Flask
from flask_cors import CORS

app = Flask(__name__, static_url_path='/static', static_folder='static')
CORS(app)

# defining routes
app.add_url_rule("/", view_func=home)
app.add_url_rule("/detect", methods=["POST"], view_func=detect)
# app.add_url_rule("/validate", methods=["POST"], view_func=validate)
app.add_url_rule("/signin", methods=["GET", "POST"], view_func=signin)
app.add_url_rule("/signup", methods=["GET", "POST"], view_func=signup)
app.add_url_rule("/details", methods=["GET"], view_func=details)
app.add_url_rule("/history", methods=["GET"], view_func=history)
app.add_url_rule("/recover/send_otp", methods=["POST"], view_func=send_otp)
app.add_url_rule("/recover/verify_otp", methods=["POST"], view_func=verify_otp)
app.add_url_rule("/verify/<path:creds>", methods=["GET"], view_func=verify)

# hadling errors with custom messages


@app.errorhandler(404)
def not_found(e):
    return {'status': 404, 'message': '404 Not Found'}, 404


@app.errorhandler(500)
def server_error(e):
    print(e)
    return {'status': 500, 'message': 'Internal Server Error'}, 500

# app.config['Resnet34'] = ResNet34
# print("Log ==>",app.config)
