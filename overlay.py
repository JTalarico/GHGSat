"""Controller for the overlay endpoint"""

import os
from flask_restful import Resource
from flask import send_file
from PIL import Image
import constants as c

def overlay_images(background_filename, foreground_filename, overlay_file):
    """Takes in an existing background and foreground file and saves to overlay file"""

    background_image = Image.open(background_filename)
    foreground_image = Image.open(foreground_filename)

    background_image = background_image.convert("RGBA")
    foreground_image = foreground_image.convert("RGBA")
    foreground_image = foreground_image.resize((background_image.size))

    background_image.paste(foreground_image, (0, 0), foreground_image)
    background_image.save(overlay_file, "PNG")

    background_image.close()
    foreground_image.close()

class Overlay(Resource):
    """Controller for overlay endpoint"""

    @classmethod
    def get(cls):
        """Get endpoint for overlay.

        Returns an image with plume overlaid
        """

        if not os.path.isfile(c.IMAGERY_FILE):
            return "Missing satelite file. Please call imagery endpoint first."

        if not os.path.isfile(c.PLUME_FILE):
            return "Missing plume file. Please upload."

        overlay_images(c.IMAGERY_FILE, c.PLUME_FILE, c.OVERLAY_FILE)

        return send_file(c.OVERLAY_FILE, mimetype="image/png")
        