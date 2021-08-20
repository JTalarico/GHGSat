from flask_restful import reqparse, Resource
from flask import Flask, send_file
import math
import requests
import Constants as c

"""
    Retruns error if lat and lon are not given as floats in url
"""
def validate_coordinates():
    parser = reqparse.RequestParser()
    parser.add_argument("lat", type=float, required=True, help="Latitude must be in the form of a number.")
    parser.add_argument("lon", type=float, required=True, help="Longitude must be in the form of a number.")
    args = parser.parse_args()
    
    return args

"""
    Takes in coordinates and filename and saves satelite image to filename
"""
def save_satelite_image(coordinates, satelite_filename):
        map_url = "{}?center={},{}&zoom=13&scale=1&size=614x320&maptype=hybrid&format=png&key={}".format(
        c.google_maps_url, coordinates["lat"], coordinates["lon"], c.google_key)
        r = requests.post(map_url)
        
        file = open(satelite_filename, "wb")
        file.write(r.content)
        file.close()


"""
    Controller for imagery endpoint
"""
class Imagery(Resource):
    def get(self):
        coordinates = validate_coordinates()
        save_satelite_image(coordinates, c.imagery_file)

        return send_file(c.imagery_file, mimetype="image/png")
