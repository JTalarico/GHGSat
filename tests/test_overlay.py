""" Tests for overlay endpoint"""

from PIL import Image, ImageChops
import overlay
import constants as c

def test_overlay_images():
    """ Overlays plume on an empty images and checks if result is expected"""

    plume = Image.open(c.PLUME_FILE)
    empty_image = Image.new("RGBA", plume.size, (255, 0, 0, 0))
    empty_image.save("tests/images/empty_image.png", "PNG")

    output_file = "tests/images/output_overlay.png"
    overlay.overlay_images("tests/images/empty_image.png", c.PLUME_FILE,
                           output_file)

    output_overlay = Image.open(output_file)
    expected_overlay = Image.open("tests/images/expected_overlay.png")

    diff = ImageChops.difference(output_overlay, expected_overlay)

    assert not diff.getbbox()
