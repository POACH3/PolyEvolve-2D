"""
polygon.py

A Polygon represents a single gene. The points are randomly
selected within the constraints provided (the dimensions of
the target image to be approximated).

NOTES:
For simplicity, initially the following will be fixed:
    - numbers of sides: 3
    - opacity: 30/255
    - colors: random

"""

from random import randint

class Polygon:
    """
    Represents a polygon defined by a set of points and a color.
    """

    def __init__(self, max_dims, vertices=None, color=None):
        """
        Args:
            max_dims (int): maximum coordinates where a polygon point may be placed.
            vertices (set): set of tuples defining the coordinates of polygon points.
            color (tuple): RGB value representing the color of the polygon.
        """
        self.max_x = max_dims[0]
        self.max_y = max_dims[1]
        self.num_vertices = 3 # all polygons will be triangles for now
        self.vertices = []

        self.vertices = vertices if vertices else self.random_vertices()
        self.color = color if color else self.random_color()

    def random_vertices(self):
        """
        Generate a set of random points.
        """
        for i in range(self.num_vertices):
            self.vertices.append(self.set_vertex())
        # connect the points (will be necessary when polygons with 4+ sides are allowed)

    def set_vertex(self):
        """
        Create a random point within constraints.

        Parameters:
            (none)

        Returns:
            tuple: A point represented by x and y coordinates.
        """
        x = randint(0, self.max_x)
        y = randint(0, self.max_y)

        point = (x, y)
        return point

    def order_vertices_cw(self):
        """
        Puts all the vertices in a clockwise order.
        """
        pass

    def random_color(self):
        """
        Get random a random color.
        RGBA format is used with opacity fixed.

        Parameters:
            (none)

        Returns:
            tuple: An RGBA color value.
        """
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        alpha = 30 # 255 is opaque

        rgba = (red, green, blue, alpha)
        return rgba

    def perturb_vertices(self):
        """
        Modifies the Polygon vertices to locations within a
        set distance (10% of the min dimension) of the original vertices.
        """
        perturb_radius = int(min(self.max_x, self.max_y) * .1)
        rand_x = randint(-perturb_radius, perturb_radius)
        rand_y = randint(-perturb_radius, perturb_radius)

        new_vertices = []
        for i in range(self.num_vertices):
            x, y = self.vertices[i]
            new_vertex = (self.clamp(x + rand_x, 0, self.max_x),
                          self.clamp(y + rand_y, 0, self.max_y))
            new_vertices.append(new_vertex)
        self.vertices = new_vertices

    def perturb_color(self):
        """
        Modifies the Polygon color to a random one within a set distance.
        """
        perturb_radius = 10

        r, g, b, a = self.color  # Unpack the existing RGBA tuple

        new_r = self.clamp(r + randint(-perturb_radius, perturb_radius), 0, 255)
        new_g = self.clamp(g + randint(-perturb_radius, perturb_radius), 0, 255)
        new_b = self.clamp(b + randint(-perturb_radius, perturb_radius), 0, 255)

        self.color = (new_r, new_g, new_b, a)

    def clamp(self, value, min_value, max_value):
        """
        Clamp values to stay within a range.
        """
        clamped_value = max(min(value, max_value), min_value)
        return clamped_value