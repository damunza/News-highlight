from flask import Flask

#instance of flask
app = Flask(__name__)

from app import views
