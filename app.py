from flask import Flask, request, make_response, redirect
from flask.helpers import url_for

app = Flask(__name__)


@app.route('/')
def inicio():
    ip_user = request.remote_addr
    response = make_response(redirect(url_for('data_user')))
    response.set_cookie('user_ip', ip_user)
    return response
    


@app.route('/data/user/')
def data_user():
    user_ip = request.cookies.get('user_ip')
    return {"hola":"sanetrox", "ip": user_ip}