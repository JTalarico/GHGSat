from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, send_file
import math
import requests
import Constants as c

def validate_coordinates():
    parser = reqparse.RequestParser()
    parser.add_argument('lat', type=float, required=True, help='Latitude must be in the form of a number.')
    parser.add_argument('lon', type=float, required=True, help='Longitude must be in the form of a number.')
    args = parser.parse_args()
    
    return args

class Imagery(Resource):
    def get(self):
        coordinates = validate_coordinates()
        mapURL = '{}?center={},{}&zoom=13&scale=1&size=640x320&maptype=hybrid&format=png&key={}'.format(
        c.googleMapsURL, coordinates['lat'], coordinates['lon'], c.googleKey)

        print(mapURL)
        r = requests.post(mapURL)
        

        file = open("satelite_image.png", "wb")
        file.write(r.content)
        file.close()

        return send_file("satelite_image.png", mimetype='image/png')
