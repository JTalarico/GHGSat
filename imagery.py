"""Controller for the imagery endpoint"""

from flask_restful import reqparse, Resource
from flask import send_file
import requests
import constants as c

def validate_coordinates():
    """Returns error if lat and lon are not given as floats in url"""

    parser = reqparse.RequestParser()
    parser.add_argument("lat", type=float, required=True,
                        help="Latitude must be in the form of a number.")
    parser.add_argument("lon", type=float, required=True,
                        help="Longitude must be in the form of a number.")
    args = parser.parse_args()

    return args

def save_satelite_image(coordinates, satelite_filename):
    """Takes in lat/lon coordinates and filename.

    Saves satelite image to filename.
    """

    map_url = "{}?center={},{}&zoom=13&scale=1&size=614x320&maptype=hybrid& \
        format=png&key={}".format(c.GOOGLE_MAPS_URL, coordinates["lat"],
                                  coordinates["lon"], c.GOOGLE_KEY)
    req = requests.post(map_url)

    file = open(satelite_filename, "wb")
    file.write(req.content)
    file.close()


class Imagery(Resource):
    """Controller for imagery endpoint"""

    @classmethod
    def get(cls):
        """Get endpoint for imagery.

        Returns an image given lat/lon in url
        """

        coordinates = validate_coordinates()
        save_satelite_image(coordinates, c.IMAGERY_FILE)

        return send_file(c.IMAGERY_FILE, mimetype="image/png")
