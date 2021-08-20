from flask_restful import reqparse, Resource
from flask import Flask, send_file
import math
import requests
import Constants as c

def validate_coordinates():
    parser = reqparse.RequestParser()
    parser.add_argument("lat", type=float, required=True, help="Latitude must be in the form of a number.")
    parser.add_argument("lon", type=float, required=True, help="Longitude must be in the form of a number.")
    args = parser.parse_args()
    
    return args

class Imagery(Resource):
    def get(self):
        coordinates = validate_coordinates()
        map_url = "{}?center={},{}&zoom=13&scale=1&size=614x320&maptype=hybrid&format=png&key={}".format(
        c.google_maps_url, coordinates["lat"], coordinates["lon"], c.google_key)
        r = requests.post(map_url)
        
        file = open(c.imagery_file, "wb")
        file.write(r.content)
        file.close()

        return send_file(c.imagery_file, mimetype="image/png")
