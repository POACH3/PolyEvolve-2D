"""
genetic_algorithm.py

Genetic Algorithm implementation on images where semi-transparent colored polygons are the genes.
"""

from random import randint

from individual import Individual
from population import Population

class GeneticAlgorithm:

    def __init__(self, target):
        self.population_size = 1000
        self.num_generations = 1000
        self.num_genes = 50
        self.population_mutation_rate = .1 # percentage likelihood for an individual to be selected
        self.genome_mutation_rate = .01 # percentage likelihood for a gene to be selected

        self.target = target
        self.target_size = target.size

        self.generations = [] # all generations containing all individuals
        # add other metrics (individual fitness, average fitness, etc)

    def run(self):
        # create generation
        self.generations.append(Population(self.target_size)) # random initial generation

        for i in range(self.num_generations):

            # measure fitness
            for j in range(self.population_size):
                # measure fitness value and record
                fitness_score = evaluate_fitness(self.generations[i][j])
                self.generations[i][j].set_fitness(fitness_score)

            # reproduce based off fitness values

            # mutate

            #generations.append(next_generation)


    def evaluate_fitness(self, individual_evaluated):
        """
        Fitness evaluation functionality used by the genetic algorithm.
        It will receive an approximation image and a target image, then measure the
        RGB distance between the two. MSE to start, but eventually will account for
        curved color space.
        """
        pass


    def crossover_two_point(self, parents):
        """
        Two-point crossover. Splits parent genomes into two or three subsets, then
        composes a child from alternating half of those subsets.

        Example:
            parent_a genome:    A1, A2, A3, A4, A5, A6
            parent_b genome:    B1, B2, B3, B4, B5, B6
            child genome:       B1, B2, A3, A4, B5, B6

        Args:
            parents (set): An array of parents (max 2 parents allowed).

        Returns:
            Individual: A new (child) Individual composed of the genes from the parents.
        """
        split_index_a = randint(0, self.num_genes - 1)
        split_index_b = randint(0, self.num_genes - 1)
        split_index_1 = min(split_index_a, split_index_b)
        split_index_2 = max(split_index_a, split_index_b)

        rand_parent = randint(0, 1)
        parent_1 = parents[rand_parent]
        parent_2 = parents[1 - rand_parent]

        gene_subset_1 = parent_1.genome[0:split_index_1]
        gene_subset_2 = parent_2.genome[split_index_1:split_index_2]
        gene_subset_3 = parent_1.genome[split_index_2:]

        new_genome = gene_subset_1 + gene_subset_2 + gene_subset_3

        child = Individual(self.target_size, genome=new_genome)
        return child
