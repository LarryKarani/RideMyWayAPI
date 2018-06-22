from flask import Flask 
from flask_restful import Api


from .routes import TestApi

"""local import"""
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    api = Api(app)

    api.add_resource(TestApi, '/')

    return app