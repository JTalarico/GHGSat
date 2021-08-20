""" GHGSat Coding Assignment
    Unit tests for overlay
 """
import Overlay
import pytest
import Constants as c
from PIL import Image, ImageChops


def test_overlay_images():
    plume = Image.open("plume.png")
    empty_image = Image.new("RGBA", plume.size, (255, 0, 0, 0))
    empty_image.save("tests/empty_image.png", "PNG")

    Overlay.overlay_images("tests/empty_image.png", c.plume_file, "tests/test_overlay.png")

    overlay = Image.open("tests/test_overlay.png")
    expected_overlay = Image.open("tests/expected_overlay.png")

    diff = ImageChops.difference(overlay, expected_overlay)

    assert not diff.getbbox()