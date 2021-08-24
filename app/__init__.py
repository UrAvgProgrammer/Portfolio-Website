import os

from flask import Flask
# from flask_bootstrap import Bootstrap


app = Flask(__name__)
# bootstrap = Bootstrap(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = os.urandom(24)

from app import views

