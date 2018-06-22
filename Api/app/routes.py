from flask import request
from flask_restful import Resource

#local imports
import json

class TestApi(Resource):
    def get(self):
        return{'hello':'kenya'}, 200