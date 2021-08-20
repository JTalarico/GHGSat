from flask_restful import abort, Resource
from flask import Flask, send_file
import math
import Constants as c
from PIL import Image
import os

"""
    Takes in an existing background and foreground file and saves to overlay file
"""
def overlay_images(background_filename, foreground_filename, overlay_filename):
    background_image = Image.open(background_filename)
    foreground_image = Image.open(foreground_filename)

    background_image = background_image.convert("RGBA")
    foreground_image = foreground_image.convert("RGBA")
    foreground_image = foreground_image.resize((background_image.size))
    
    background_image.paste(foreground_image, (0, 0), foreground_image)
    background_image.save(overlay_filename,"PNG")
    
    background_image.close()
    foreground_image.close()

"""
    Controller for overlay endpoint
"""
class Overlay(Resource):
    def get(self):
        if not os.path.isfile(c.imagery_file):
            return "Missing satelite file. Please call imagery endpoint first."

        if not os.path.isfile(c.plume_file):
            return "Missing plume file. Please upload."

        overlay_images(c.imagery_file, c.plume_file, c.overlay_file)

        return send_file(c.overlay_file, mimetype="image/png")