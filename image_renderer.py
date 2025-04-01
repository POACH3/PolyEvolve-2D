"""
image_renderer.py

Used by genetic_algorithm.py to create candidate images.
Also responsible for image I/O and display.
"""

from PIL import Image
from PIL import ImageDraw

class ImageRenderer:
    def load_image(self, path):
        """Load an image from the given path using Pillow."""
        return Image.open(path)

    def save_image(self, image, path):
        """Save the image to the specified path."""
        image.save(path)

    def show_image(self, image):
        """
        Display the image.

        Parameters:
            image (Image)

        Returns:

        """
        return image.show()

    def create_image(self, individual):
        """
        Create an image from the given individual using Pillow.

        Parameters:
            individual (Individual): The individual to be rendered.

        Returns:
            (Image): The rendered Pillow Image.
        """
        image = Image.new("RGBA", individual.size, (0, 0, 0, 255)) # black, opaque background
        draw = ImageDraw.Draw(image, "RGBA")

        for polygon in individual.genome:
            draw.polygon(polygon.vertices, fill=polygon.color)

        return image

    def convert_image(self, image):
        return image.convert("RGBA")