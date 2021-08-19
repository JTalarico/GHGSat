from flask import Flask
from flask_restful import Resource, Api
from Imagery import Imagery
from Overlay import Overlay

app = Flask(__name__)
api = Api(app)

api.add_resource(Imagery, '/imagery')
api.add_resource(Overlay, '/overlay')

if __name__ == '__main__':
    app.run(debug=True)