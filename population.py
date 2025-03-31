"""
population.py

A Population represents a generation of candidate solutions (collections
of genes) that approximate a target image.

NOTES:
For simplicity, initially the following will be fixed:
    - generation size: 1000

Possibly merge class into genetic_algorithm.py and represent as a list.
"""

from individual import Individual

class Population:
    """
    Represents a generation defined by a set Individuals.
    """

    def __init__(self, max_dims):
        self.generation_size = 1000
        self.population_fitness_score = -1 # average fitness

        self.individuals = []
        for i in range(self.generation_size):
            individual = Individual(max_dims)
            self.individuals.append(individual)

    def set_fitness(self, average_fitness):
        self.population_fitness_score = average_fitness