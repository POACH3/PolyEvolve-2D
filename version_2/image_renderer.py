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

        An image is created for each gene and then merged to image for
        the individual.

        Parameters:
            individual (Individual): The individual to be rendered.

        Returns:
            (Image): The rendered Pillow Image.
        """
        image_individual = Image.new("RGBA", individual.size, (0, 0, 0, 255)) # black, opaque background
        #image_individual = Image.new("RGBA", individual.size, (255, 255, 255, 0))  # white, transparent background
        #draw = ImageDraw.Draw(image_individual, "RGBA")

        for polygon in individual.genome:
            image_gene = Image.new("RGBA", individual.size, (255, 255, 255, 0))  # white, transparent background
            draw = ImageDraw.Draw(image_gene, "RGBA")
            draw.polygon(polygon.vertices, fill=polygon.color)

            # stack and blend the images
            image_individual = Image.alpha_composite(image_individual, image_gene)

        return image_individual

    def convert_image(self, image):
        return image.convert("RGBA")

    def test(self):
        image = Image.new("RGBA", (200, 200), (255, 255, 255, 255))
        draw = ImageDraw.Draw(image, "RGBA")
        # Draw green triangle at 50% opacity
        draw.polygon([(0, 50), (120, 20), (100, 200)], fill=(0, 255, 0, 30))
        # Draw red triangle on top at 50% opacity
        draw.polygon([(50, 50), (150, 50), (100, 150)], fill=(255, 0, 0, 0))
        image.save("output.png")