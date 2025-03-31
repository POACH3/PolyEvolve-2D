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

    def __init__(self, size, genome=None, num_genes=50):
        self.size = size
        self.num_genes = num_genes
        self.fitness_score = -1

        self.genome = genome if genome else self.random_genome()

    def random_genome(self):
        """
        Generates a random genome for an individual.
        """
        for i in range(self.num_genes):
            polygon = Polygon(self.size)
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

    def set_fitness(self, fitness_score):
        self.fitness_score = fitness_score