from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.wrappers import Response


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/Ireniza/Desktop/database-cet/database.db" 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
