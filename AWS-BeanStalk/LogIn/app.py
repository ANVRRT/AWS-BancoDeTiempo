import json
from flask import Flask, render_template, request,redirect
from flask.helpers import url_for
import requests
#from requests.api import request
from LogIn.user import get_user
from flask_login import LoginManager,login_user,current_user
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from werkzeug.security import generate_password_hash, check_password_hash
from user import users
from werkzeug.urls import url_parse
import forms

app= Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.static_folder='static'
login_manager = LoginManager(app)

bootstrap = Bootstrap(app)
moment = Moment(app)

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None


@app.route('/Inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/',methods=['GET','POST'])
def login():
    idUsuario=None
    password=None
    msg=""
    form = forms.LoginForm()
    if form.validate_on_submit():
        idUsuario=form.user_id.data
        password=form.password.data
        data= {
            "username": idUsuario,
            "password":password
        }
        
        respose = requests.post("https://bka70s5pka.execute-api.us-east-1.amazonaws.com/beta",json.dumps(data))
        respose=json.loads(respose.content)

        if(respose["loginApproval"]):
            return redirect(url_for('inicio'))
        else:
            msg="Usuario o contraseña incorrecto"
            print(msg)
    return render_template('login.html', form=form,msg=msg)