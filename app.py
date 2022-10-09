from api.home import home
from api.auth.signup import signup
from api.auth.signin import signin
from api.features.log.retrieve import retrieve
from api.features.log.save import save
from api.features.validate import validate
from api.features.detect import detect

from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

app.add_url_rule("/", view_func=home)
app.add_url_rule("/detect", view_func=detect)
app.add_url_rule("/validate", view_func=validate)
app.add_url_rule("/signin", view_func=signin)
app.add_url_rule("/signup", view_func=signup)
app.add_url_rule("/log/save", view_func=save)
app.add_url_rule("/log/retrieve", view_func=retrieve)


@app.errorhandler(404)
def not_found(e):
    return render_template('404/404.html')
