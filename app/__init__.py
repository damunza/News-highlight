from flask import Flask
from .config import DevConfig


#instance of flask
app = Flask(__name__)

#after importin Devconfig
app.config.from_object(DevConfig)

from app import views
