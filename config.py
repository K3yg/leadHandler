from flask import Flask, render_template, request, send_file, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os, datetime
from werkzeug.wrappers import Response
from flask_login import UserMixin, LoginManager, login_manager, login_user, login_required, logout_user, current_user
from wtforms.validators import DataRequired ,InputRequired, ValidationError, Length
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from flask_wtf import FlaskForm
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/Gessica/Desktop/Plat-Cet-main/database.db"

caminho = os.path.dirname(os.path.abspath(__file__))    
arquivobd = os.path.join(caminho, "users.db") 

app.config["SQLALCHEMY_BINDS"] = {'users': 'sqlite:///'+arquivobd}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "ygbr*&qybgrf3$u417nbg7d@adsi"
db = SQLAlchemy(app)
