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
        self.fitness = -1

        self.genome = genome if genome else self.random_genome()

    def random_genome(self):
        """
        Generates a random genome for an individual.
        """
        rand_genome = []

        for i in range(self.num_genes):
            polygon = Polygon(self.size)
            rand_genome.append(polygon)

        return rand_genome


    def mutate_gene(self, gene_mutation_rate):
        """
        Modifies a random gene (Polygon) in the genome (Individual) by perturbing
        the vertices and color of a Polygon to a new value within a set radius.
        """
        num_mutations = int(self.num_genes * gene_mutation_rate)
        gene_mutate_indices = []

        for i in range(num_mutations):
            gene_idx = randint(0, self.num_genes - 1)

            while gene_idx in gene_mutate_indices:
                gene_idx = randint(0, self.num_genes - 1)
            gene_mutate_indices.append(gene_idx)

            gene = self.genome[gene_idx]
            mutate_type = randint(0, 2)
            if mutate_type == 0:
                gene.perturb_vertices()
            elif mutate_type == 1:
                gene.add_vertex() # should scale with the number of vertices in the polygon
            elif mutate_type == 2:
                gene.perturb_color()

    def replace_gene(self):
        """
        Replaces a random gene (Polygon) in the genome (Individual).
        """
        gene_index = randint(0, self.num_genes - 1)

        self.genome.pop(gene_index)
        self.genome.insert(gene_index, Polygon(self.size))

    def set_fitness(self, fitness_score):
        self.fitness = fitness_score