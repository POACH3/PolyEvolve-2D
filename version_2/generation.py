"""
population.py

A Population represents a generation of candidate solutions (collections
of genes) that approximate a target image.

NOTES:
For simplicity, initially the following will be fixed:
    - generation size: 1000

Possibly merge class into genetic_algorithm.py and represent as a list.
"""

from version_2.individual import Individual

class Generation:
    """
    Represents a generation defined by a set Individuals.
    """

    def __init__(self, individual_size, individuals, population_size=1000):
        self.population_size = population_size
        self.population_fitness_score = -1 # average fitness
        self.individual_size = individual_size

        self.population = individuals if individuals else self.random_individuals()

    def random_individuals(self):
        """
        Generates a random set of individuals.
        """
        new_individuals = []

        for i in range(self.population_size):
            individual = Individual(self.individual_size)
            new_individuals.append(individual)

        return new_individuals

    def set_fitness(self, average_fitness):
        self.population_fitness_score = average_fitness

    def order_by_fitness(self):
        """
        Orders the population by individual fitness score (descending).
        """
        self.population.sort(key=lambda individual: individual.fitness, reverse=True)

    def __iter__(self):
        return iter(self.population)