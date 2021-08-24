""" Tests for imagery endpoint"""

from PIL import Image, ImageChops
import imagery

def test_save_satelite_image():
    """ Retrieves and saves the satelite image and compares to expected result"""

    coordinates = {"lat": 80.2, "lon": 32.5}
    imagery.save_satelite_image(coordinates, "tests/images/output_imagery.png")

    expected_imagery = Image.open("tests/images/expected_imagery.png")
    output_imagery = Image.open("tests/images/output_imagery.png")

    diff = ImageChops.difference(expected_imagery, output_imagery)

    assert not diff.getbbox()
