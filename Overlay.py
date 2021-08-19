from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, send_file
import math
import requests
import Constants as c
from PIL import Image

class Overlay(Resource):
    def get(self):
        imageryFile = Image.open(c.imageryFile)
        plume = Image.open(c.plumeFile)
        imageryFile.paste(plume, (0,0))
        return send_file(imageryFile, mimetype='image/png')
