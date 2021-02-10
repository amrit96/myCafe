from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafe.sqlite3'

db = SQLAlchemy(app)

from my_cafe.views import stockAPI
from my_cafe.models import Profile, RawPurchase