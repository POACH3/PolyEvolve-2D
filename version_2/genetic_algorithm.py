"""
genetic_algorithm.py

Genetic Algorithm implementation on images where semi-transparent colored polygons are the genes.

NOTES:
    Fitness function is MSE to start, but eventually will account for curved color space.

"""

import copy
import numpy as np
from random import randint
from version_2.image_renderer import ImageRenderer
from version_2.individual import Individual
from version_2.generation import Generation

class GeneticAlgorithm:

    def __init__(self, target):
        self.population_size = 100
        self.num_generations = 150
        self.num_genes = 50 # 50?
        self.num_elites = 30 # 15-25% of most fit Individuals copied to next generation
        self.population_mutation_rate = .01 # 5-10% likelihood for an individual to be selected
        self.genome_mutation_rate = .25 # 25% likelihood for a gene to be selected

        self.target = target # the png provided
        self.target_size = target.size

        self.elite_individual = None # random initialization
        self.generations = [] # all generations containing all individuals


    def evolve(self):
        """
        Runs the genetic algorithm.
        """

        # random initialization
        self.elite_individual = Individual(self.target_size, num_genes=self.num_genes)

        for gen in range(self.num_generations):
            print(f"Generation {gen}")
            # generate replacement candidates
            self.generations.append(self.reproduce())

            #for ind in self.generations[gen].individuals:
            for ind in self.generations[gen]:
                # evaluate candidates
                #score = self.evaluate_fitness_mse(self.generations[gen].individuals[ind])
                score = self.evaluate_fitness_mse(ind)
                #self.generations[gen].individuals[ind].set_fitness(score)
                ind.set_fitness(score)

            # sort by fitness
            self.generations[gen].order_by_fitness()

            # replace if necessary
            most_fit = self.generations[gen].population[0] # most fit of the generation
            if most_fit.fitness > self.elite_individual.fitness:
                self.elite_individual = most_fit

            # save image of most fit Individual
            ir = ImageRenderer()
            file_name = f"gen{len(self.generations)}"
            ir.save_image(ir.create_image(self.elite_individual), f"./polyevolve_images/{file_name}.png")

    def evaluate_fitness_mse(self, individual):
        """
        Fitness evaluation functionality using MSE in RGB space.
        Calculates the error between each corresponding pixel in the
        approximation and target images by summing the squared errors for
        each color channel of a pixel, then averaging the result across all pixels.

        Args:
            individual (Individual): The candidate individual to be evaluated.

        Returns:
            (int): The fitness score (higher is better).

        """
        target_rgb = self.target.convert('RGBA')

        renderer = ImageRenderer()
        individual_image = renderer.create_image(individual)
        individual_rgb = renderer.convert_image(individual_image)

        target_arr = np.array(target_rgb).astype(np.int32)
        individual_arr = np.array(individual_rgb).astype(np.int32)

        squared_error = (target_arr[:,:,:3] - individual_arr[:,:,:3]) ** 2
        mse = np.mean(np.sum(squared_error, axis=2))
        assert mse >= 0, "MSE must be non-negative"

        max_possible_mse = 195075
        fitness_score = max_possible_mse - mse
        #print(f"{fitness_score}\n")                                                                        #FIXME
        return fitness_score

    def reproduce(self):
        """
        Creates a new generation of Individuals using asexual reproduction and mutation.
        A clone of the elite Individual is created, then mutated.

        Returns:
            (Generation): The new generation of Individuals.
        """
        new_individuals = []

        # clone elite
        for _ in range(self.population_size):
            new_individual = copy.deepcopy(self.elite_individual)
            new_individuals.append(new_individual)

        new_generation = Generation(self.target_size, individuals=new_individuals, population_size=self.population_size)

        # mutate clones
        for individual in new_generation:
            individual.mutate(self.genome_mutation_rate)

        #self.generations.append(new_generation)
        return new_generation

    def mutate(self, generation):
        """
        Mutates select individuals from a generation.

        Args:
            generation: A population of individuals.

        """
        num_mutate = int(self.population_mutation_rate * self.population_size)
        mutate_indices = set()

        while len(mutate_indices) < num_mutate:
            selected_index = randint(0, self.population_size - 1)
            mutate_indices.add(selected_index)

        for index in mutate_indices:
            generation.individuals[index].mutate_gene()