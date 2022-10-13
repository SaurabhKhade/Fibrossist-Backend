from api.home import home
from api.auth.signup import signup
from api.auth.signin import signin
from api.features.log.retrieve import retrieve
from api.features.log.save import save
from api.features.validate import validate
from api.features.detect import detect

from flask import Flask
app = Flask(__name__, static_url_path='/static')

app.add_url_rule("/", view_func=home)
app.add_url_rule("/detect", methods=["POST"], view_func=detect)
app.add_url_rule("/validate", methods=["POST"], view_func=validate)
app.add_url_rule("/signin", methods=["POST"], view_func=signin)
app.add_url_rule("/signup", methods=["POST"], view_func=signup)
app.add_url_rule("/log/save", methods=["POST"], view_func=save)
app.add_url_rule("/log/retrieve", methods=["GET"], view_func=retrieve)


@app.errorhandler(404)
def not_found(e):
    return {'status': 404, 'message': '404 Not Found'}, 404


@app.errorhandler(500)
def server_error(e):
    print(e)
    return {'status': 500, 'message': 'Internal Server Error'}, 500
