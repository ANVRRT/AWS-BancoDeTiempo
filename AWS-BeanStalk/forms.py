
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    user_id = StringField('Usuario:', validators=[DataRequired()])
    password = PasswordField('Contraseña:', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')
