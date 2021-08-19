from flask import Flask
from flask_restful import Resource, Api
from Imagery import Imagery

app = Flask(__name__)
api = Api(app)

api.add_resource(Imagery, '/imagery')

if __name__ == '__main__':
    app.run(debug=True)