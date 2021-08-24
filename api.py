"""Defines the flask REST api for the assignment"""

from flask import Flask
from flask_restful import Api
from imagery import Imagery
from overlay import Overlay

APP = Flask(__name__)
API = Api(APP)

API.add_resource(Imagery, '/imagery')
API.add_resource(Overlay, '/overlay')

if __name__ == '__main__':
    APP.run(debug=True)
