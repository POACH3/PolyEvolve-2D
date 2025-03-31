"""
individual.py

An Individual represents a candidate genome (a collection of genes) that
approximates a target image. The "genes" are Polygons randomly
generated within the constraints provided (the dimensions of
the target image to be approximated).

NOTES:
For simplicity, initially the following will be fixed:
    - numbers of polygons: 50

Gene mutation options:
    - replace whole polygons
    - change points and colors of polygons

"""

from random import randint
from polygon import Polygon

class Individual:
    """
    Represents a candidate image defined by a set of Polygons.
    """

    def __init__(self, max_dims):
        self.max_dims = max_dims
        self.num_genes = 50
        self.genome = []

        for i in range(self.num_genes):
            polygon = Polygon(max_dims)
            self.genome.append(polygon)

    def mutate(self):
        """
        Modifies a random gene (Polygon) in the genome (Individual).
        """
        gene_num = randint(0, self.num_genes - 1)

        # mutate gene
        #gene = self.genome[gene_num]
        #gene.mutate()

        # replace gene (mutate genome)
        self.genome.pop(gene_num)
        self.genome.insert(gene_num, Polygon(self.max_dims))
