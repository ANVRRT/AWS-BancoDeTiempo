import json
from flask import Flask, render_template, request,redirect,g
from flask.helpers import url_for
from flask.wrappers import Response
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
import hashlib
from functools import wraps
from flask_cors import CORS
import base64

app= Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'hard to guess string'
app.static_folder='static'
login_manager = LoginManager(app)

bootstrap = Bootstrap(app)
moment = Moment(app)
user=None

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

def login_required(f):
    global user
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if user is None:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/LoadImg/<data>',methods=['GET','POST'])
def loadImg(data):
    data.encode("utf-8")
    data=base64.b64decode(data)
    data=json.loads(data)
    print(data)
    return(render_template('formHelpers.html',data=data,base=base64))

@app.route('/Perfil/<data>',methods=['GET','POST'])
@login_required
def perfil(data):
    data.encode("utf-8")
    data=base64.b64decode(data)
    data=json.loads(data)
    
    return(render_template('perfilUsuario.html',data=data,base=base64,json=json))




@app.route('/Inicio',methods=['GET','POST'])
@login_required
def inicio():
    headings = ("Usuario", "Nombre", "Apellido", "Identificacion",
    "Comprobante de domicilio","Carta de antecedentes no penales","Aprobar")
    respose = requests.post("https://bka70s5pka.execute-api.us-east-1.amazonaws.com/API/getusers","")
    respose=json.loads(respose.content)
   
    
    return render_template('inicio.html', headings=headings, dataT=respose,json=json, base=base64)
    
@app.route('/',methods=['GET','POST'])
def login():
    global user
    user=None
    idUsuario=None
    password=None
    msg=""
    form = forms.LoginForm()
    if form.validate_on_submit():
        idUsuario=form.user_id.data
        password=form.password.data
        password=password.encode('utf-8')
        h=hashlib.new("sha256",password)
        data= {
            "username": idUsuario,
            "password":h.hexdigest()
        }
        
        respose = requests.post("https://bka70s5pka.execute-api.us-east-1.amazonaws.com/API/loginadmin",json.dumps(data))
        respose=json.loads(respose.content)
        print(respose)
        if(respose["loginApproval"]):
            user=idUsuario
            return redirect(url_for('inicio'))
        else:
            msg="Usuario o contraseña incorrecto"
            print(msg)
    return render_template('login.html', form=form,msg=msg)