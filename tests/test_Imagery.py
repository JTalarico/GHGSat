""" GHGSat Coding Assignment
    Unit tests for overlay
 """
import Imagery
import pytest
import Constants as c
from PIL import Image, ImageChops


def test_save_satelite_image():
    coordinates = {"lat": 45.5, "lon": -73.6}
    Imagery.save_satelite_image(coordinates, "tests/images/output_imagery.png")
    
    expected_imagery = Image.open("tests/images/expected_imagery.png")
    output_imagery = Image.open("tests/images/output_imagery.png")

    diff = ImageChops.difference(expected_imagery, output_imagery)

    assert not diff.getbbox()