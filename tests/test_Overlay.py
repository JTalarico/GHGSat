""" GHGSat Coding Assignment
    Unit tests for overlay
 """
import Overlay
import pytest
import Constants as c
from PIL import Image, ImageChops


def test_overlay_images():
    plume = Image.open("images/plume.png")
    empty_image = Image.new("RGBA", plume.size, (255, 0, 0, 0))
    empty_image.save("tests/images/empty_image.png", "PNG")

    output_file = "tests/images/output_overlay.png"
    Overlay.overlay_images("tests/images/empty_image.png", c.plume_file, output_file)

    output_overlay = Image.open(output_file)
    expected_overlay = Image.open("tests/images/expected_overlay.png")

    diff = ImageChops.difference(output_overlay, expected_overlay)

    assert not diff.getbbox()