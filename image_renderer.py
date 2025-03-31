"""
image_renderer.py

Used by genetic_algorithm.py to create candidate images.
Also responsible for image I/O and display.
"""

from PIL import Image

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
