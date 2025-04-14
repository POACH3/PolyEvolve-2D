"""
gene.py

A Gene represents a single gene. It is a polygon where
the points are randomly selected within the
constraints provided (the dimensions of the target image to be approximated).

NOTES:

"""

from random import randint
from shapely.geometry import Polygon
import math

class Gene:
    """
    Represents a polygon defined by a set of points and a color.
    """

    def __init__(self, max_dims, vertices=None, color=None):
        """
        Args:
            max_dims (tuple): maximum coordinates where a polygon point may be placed.
            vertices (list): tuples defining the coordinates of polygon points.
            color (tuple): RGB value representing the color of the polygon.
        """
        self.max_x = max_dims[0]
        self.max_y = max_dims[1]
        self.num_vertices = 3

        self.vertices = vertices if vertices else self.random_points()
        self.color = color if color else self.random_color()

        #self.sp

    def random_points(self):
        """
        Generate a set of random points. They must form a simple polygon.
        """
        while True:
            points = []
            for i in range(self.num_vertices):
                points.append(self.random_point())

            if self.valid_shape(points):
                break

        self.order_cw(points)

        return points

    def random_point(self):
        """
        Create a random point within constraints.

        Returns:
            tuple: A point represented by x and y coordinates.
        """
        x = randint(0, self.max_x)
        y = randint(0, self.max_y)

        point = (x, y)
        return point

    def add_vertex(self):
        """
        Add a vertex to the polygon by taking the midpoint of two random
        adjacent vertices and perturbing it.
        """
        attempts = 0
        #while True:
        while attempts < 100:
            rand = randint(0, self.num_vertices - 2) # a little janky
            v1 = self.vertices[rand]
            v2 = self.vertices[rand+1]

            new_vertex = ((v1[0] + v2[0]) // 2, (v1[1] + v2[1]) // 2)
            perturb_radius = int(min(self.max_x, self.max_y) * .05)
            new_vertex_perturbed = self.perturb_vertex(new_vertex, perturb_radius)

            new_vertices = self.vertices.copy()
            new_vertices.append(new_vertex_perturbed)

            if self.valid_shape(new_vertices):
                self.num_vertices += 1
                self.vertices = self.order_cw(new_vertices)
                #self.sp = Polygon(self.vertices)
                break

            attempts += 1

    def valid_shape(self, vertices):
        """
        Check if the polygon is valid (non-zero area, no duplicate vertices) and simple.
        """
        sp = Polygon(vertices) # a Shapely polygon

        if sp.is_simple and sp.is_valid:
            return True
        else:
            return False

    def order_cw(self, points):
        """
        Puts all the points in a clockwise order.
        """
        sp = Polygon(points)
        cx = sp.centroid.x
        cy = sp.centroid.y

        def angle_about_centroid(point):
            px, py = point
            return math.atan2(py - cy, px - cx)

        return sorted(points, key=angle_about_centroid, reverse=True)

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
        alpha = 60 # 255 is opaque

        rgba = (red, green, blue, alpha)
        return rgba

    def perturb_vertices(self):
        """
        Modifies the Polygon vertices to locations within a set
        distance (percentage of the min canvas dimension) of the original vertices.
        """
        perturb_radius = int(min(self.max_x, self.max_y) * .1)

        new_vertices = []
        for i in range(self.num_vertices):
            new_vertex = self.perturb_vertex(self.vertices[i], perturb_radius)
            new_vertices.append(new_vertex)

        self.vertices = new_vertices

    def perturb_vertex(self, vertex, radius):
        """
        Modifies a vertex to a location within a provided radius.
        """
        rand_x = randint(-radius, radius)
        rand_y = randint(-radius, radius)

        x, y = vertex
        new_vertex = (self.clamp(x + rand_x, 0, self.max_x),
                      self.clamp(y + rand_y, 0, self.max_y))

        return new_vertex

    def perturb_color(self):
        """
        Modifies the Polygon color to a random one within a set distance.
        """
        perturb_radius = 10

        r, g, b, a = self.color  # Unpack the existing RGBA tuple

        new_r = self.wrap(r + randint(-perturb_radius, perturb_radius), 0, 255)
        new_g = self.wrap(g + randint(-perturb_radius, perturb_radius), 0, 255)
        new_b = self.wrap(b + randint(-perturb_radius, perturb_radius), 0, 255)

        self.color = (new_r, new_g, new_b, a)

    def clamp(self, value, min_value, max_value):
        """
        Clamp values to stay within a range.
        """
        clamped_value = max(min(value, max_value), min_value)
        return clamped_value

    def wrap(self, value, min_value, max_value):
        """
        Wrap values around space to stay within a range.
        """
        wrapped_value = -1

        if value < min_value:
            #wrapped_value = max_value - abs(value - min_value)
            wrapped_value = max_value + (value - min_value)
        elif value > max_value:
            wrapped_value = min_value + (value - max_value)

        return wrapped_value