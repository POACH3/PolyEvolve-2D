"""
polygon.py

A Polygon represents a single gene. The points are randomly
selected within the constraints provided (the dimensions of
the target image to be approximated).

NOTES:
For simplicity, initially the following will be fixed:
    - numbers of sides: 3
    - opacity: 50%
    - colors: random

"""

from random import randint

class Polygon:
    """
    Represents a polygon defined by a set of points and a color.
    """

    def __init__(self, max_dim_x, max_dim_y):
        self.max_dim_x = max_dim_x
        self.max_dim_y = max_dim_y

        points = []
        for i in range(3): # all polygons will be triangles for now
            points.append(self.set_point())
        # connect the points (will be necessary when polygons with 4+ sides are allowed)
        self.color = self.set_color()

    def set_point(self):
        """
        Get a random point within constraints.

        Parameters:
            (none)

        Returns:
            tuple: A point represented by x and y coordinates.
        """
        x = randint(0, self.max_dim_x)
        y = randint(0, self.max_dim_y)

        point = (x, y)
        return point

    def set_edges(self):
        """
        Connect all points with edges that don't cross.
        """
        return

    def set_color(self):
        """
        Get random a random color.
        RGBA format is used with opacity fixed at 50%.

        Parameters:
            (none)

        Returns:
            tuple: An RGBA color value.
        """
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        alpha = .5

        rgba = (red, green, blue, alpha)
        return rgba