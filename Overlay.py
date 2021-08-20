from flask_restful import abort, Resource
from flask import Flask, send_file
import math
import Constants as c
from PIL import Image
import os

class Overlay(Resource):
    def get(self):
        if not os.path.isfile(c.imagery_file):
            return "Missing satelite file. Please call imagery endpoint first."

        satelite_image = Image.open(c.imagery_file)
        plume_image = Image.open(c.plume_file)

        satelite_image = satelite_image.convert("RGBA")
        plume_image = plume_image.convert("RGBA")
        plume_image = plume_image.resize((satelite_image.size))

        satelite_image.paste(plume_image, (0, 0), plume_image)
        satelite_image.save(c.overlay_file,"PNG")

        satelite_image.close()
        plume_image.close()

        return send_file(c.overlay_file, mimetype="image/png")
