"""
genetic_algorithm.py

Genetic Algorithm implementation on images where semi-transparent colored polygons are the genes.
"""

from population import Population

class GeneticAlgorithm:
    """
    def __init__(self, population_size, num_generations):
        self.population_size = population_size
        self.num_generations = num_generations
    """
    def __init__(self, target):
        self.population_size = 1000
        self.num_generations = 100
        self.mutation_rate = .01 # percentage
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