from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig


#instance of flask
app = Flask(__name__, instance_relative_config = True)

#after importing Devconfig
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#making an instance of bootstrap
bootstrap = Bootstrap(app)

from app import views
