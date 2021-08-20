from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, send_file
import math
import requests
import Constants as c
from PIL import Image

class Overlay(Resource):
    def get(self):
        if os.path.isfile(c.imageryFile):
            abort

        sateliteImage = Image.open(c.imageryFile)
        plumeImage = Image.open(c.plumeFile)

        sateliteImage = sateliteImage.convert("RGBA")
        plumeImage = plumeImage.convert("RGBA")
        plumeImage = plumeImage.resize((sateliteImage.size))

        sateliteImage.paste(plumeImage, (0, 0), plumeImage)
        sateliteImage.save(c.overlayFile,"PNG")

        sateliteImage.close()
        plumeImage.close()

        return send_file(c.overlayFile, mimetype='image/png')
