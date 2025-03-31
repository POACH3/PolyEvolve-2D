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

    def __init__(self, max_dims):
        self.max_x = max_dims[0]
        self.max_y = max_dims[1]
        self.num_points = 3 # all polygons will be triangles for now

        points = []
        for i in range(self.num_points):
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
        x = randint(0, self.max_x)
        y = randint(0, self.max_y)

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

    def mutate(self):
        """
        Modifies the Polygon points and color.
        """
        new_points = []
        for i in range(self.num_points):
            new_points.append(self.set_point())
        self.points = new_points

        new_color = self.set_color()
        self.color = new_color