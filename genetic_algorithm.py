"""
genetic_algorithm.py

Genetic Algorithm implementation on images where semi-transparent colored polygons are the genes.

NOTES:
    Fitness function is MSE to start, but eventually will account for curved color space.
    Consider converting to NumPy array for fitness measurement.

"""

import numpy as np
from random import randint
from image_renderer import ImageRenderer
from individual import Individual
from population import Population

class GeneticAlgorithm:

    def __init__(self, target):
        self.population_size = 500
        self.num_generations = 500
        self.num_genes = 50
        self.num_elites = 3 # 3 most fit Individuals copied to next generation
        self.population_mutation_rate = .1 # percentage likelihood for an individual to be selected
        self.genome_mutation_rate = .01 # percentage likelihood for a gene to be selected

        self.target = target
        self.target_size = target.size

        self.generations = [] # all generations containing all individuals
        # add other metrics (individual fitness, average fitness, etc)

    def evolve(self):
        """
        Runs the genetic algorithm.
        """
        self.generations.append(Population(individual_size=self.target_size, population_size=self.population_size)) # random initial generation

        for population in range(self.num_generations):
            for individual in range(self.population_size):

                # measure fitness and record
                score = self.evaluate_fitness_mse(self.generations[population].individuals[individual])
                self.generations[population].individuals[individual].set_fitness(score)

            # reproduce based off fitness scores
            self.generations.append(self.reproduce(self.generations[-1]))

            # mutate
            self.mutate(self.generations[-1])

    def evaluate_fitness_abs_diff(self, individual):
        """
        Fitness evaluation functionality using the sum of absolute
        differences in RGB space.
        Measures distances between each corresponding pixel in
        the approximation and target images.

        Args:
            individual (Individual): The candidate individual to be evaluated.

        Returns:
            (int): The fitness score (higher is better).

        """
        total_error = 0

        target_rgb = self.target.convert('RGBA')

        renderer = ImageRenderer()
        individual_image = renderer.create_image(individual)
        individual_rgb = renderer.convert_image(individual_image)

        for x in range(self.target_size[0]):
            for y in range(self.target_size[1]):
                target_pixel = target_rgb.getpixel((x,y))
                target_red, target_green, target_blue, _ = target_pixel

                individual_pixel = individual_rgb.getpixel((x,y))
                individual_red, individual_green, individual_blue, _ = individual_pixel

                red_error = abs(target_red - individual_red)
                green_error = abs(target_green - individual_green)
                blue_error = abs(target_blue - individual_blue)

                pixel_error = red_error + green_error + blue_error
                total_error += pixel_error

        fitness_score = 1 / (total_error + 1e-6)
        return fitness_score

    def evaluate_fitness_mse(self, individual):
        """
        Fitness evaluation functionality using MSE in RGB space.
        Calculates the error between each corresponding pixel in the
        approximation and target images by summing the squared errors for
        each color channel of a pixel, then averaging the result across all pixels.

        Args:
            individual (Individual): The candidate individual to be evaluated.

        Returns:
            (int): The fitness score (lower is better).

        """
        total_error = 0

        width, height = individual.size
        num_pixels = width * height

        target_rgb = self.target.convert('RGBA')

        renderer = ImageRenderer()
        individual_image = renderer.create_image(individual)
        individual_rgb = renderer.convert_image(individual_image)

        for x in range(self.target_size[0]):
            for y in range(self.target_size[1]):
                target_pixel = target_rgb.getpixel((x,y))
                target_red, target_green, target_blue, _ = target_pixel

                individual_pixel = individual_rgb.getpixel((x,y))
                individual_red, individual_green, individual_blue, _ = individual_pixel

                red_error = (target_red - individual_red) ** 2
                green_error = (target_green - individual_green) ** 2
                blue_error = (target_blue - individual_blue) ** 2

                pixel_error = red_error + green_error + blue_error
                total_error += pixel_error

        average_pixel_error = total_error / num_pixels
        fitness_score = 1 / (average_pixel_error + 1e-6)
        #print(f"{fitness_score}\n")                                                                        #FIXME
        return fitness_score

    def reproduce(self, population):
        """
        Creates a new generation of Individuals using elites from the
        last generation and gene crossover.

        Args:
            population (Population): The current generation of Individuals.

        Returns:
            (Population): The new generation of Individuals.
        """
        new_individuals = []

        # select elites
        population.order_by_fitness()
        new_individuals.extend(population.individuals[:self.num_elites])

        # save image of most fit Individual
        ir = ImageRenderer()
        file_name = f"most_fit_gen{len(self.generations)}"
        ir.save_image(ir.create_image(population.individuals[0]), f"./polyevolve_images/{file_name}.png")

        # crossover based on fitness
        for i in range(self.population_size - self.num_elites):
            parent_a = self.select_parent(population)
            parent_b = self.select_parent(population)
            while parent_b == parent_a:
                parent_b = self.select_parent(population)

            parents = [parent_a, parent_b]

            child = self.crossover_two_point(parents)
            new_individuals.append(child)

        new_generation = Population(individual_size=self.target_size, individuals=new_individuals)
        return new_generation

    def select_parent(self, population):
        """
        Selects a parent probabilistically based on fitness.

        Args:
            population (Population): The population from which to select a parent.

        Returns:
            (Individual): The selected parent.
        """
        fitnesses = np.array([individual.fitness for individual in population.individuals])
        #print(f"Fitnesses count: {len(fitnesses)}\n\n")                                                          #FIXME
        #print(f"population count: {len(population.individuals)}\n\n")
        total_population_fitness = fitnesses.sum()
        probabilities = fitnesses / total_population_fitness
        #print(probabilities)                                                                            #FIXME

        #selected_index = np.random.choice(self.population_size, p=probabilities)
        selected_index = np.random.choice(len(population.individuals), p=probabilities)
        selected_parent = population.individuals[selected_index]
        return selected_parent

    def crossover_two_point(self, parents):
        """
        Two-point crossover. Splits parent genomes into two or three subsets, then
        composes a child from alternating half of those subsets.

        Example:
            parent_a genome:    A1, A2, A3, A4, A5, A6
            parent_b genome:    B1, B2, B3, B4, B5, B6
            child genome:       B1, B2, A3, A4, B5, B6

        Args:
            parents (list): A list of parents (max 2 parents allowed).

        Returns:
            (Individual): A new (child) Individual composed of the genes from the parents.
        """
        a = randint(0, self.num_genes)
        b = randint(0, self.num_genes)
        split_index_1 = min(a, b)
        split_index_2 = max(a, b)

        rand_parent = randint(0, 1)
        parent_1 = parents[rand_parent]
        parent_2 = parents[1 - rand_parent]

        gene_subset_1 = parent_1.genome[0:split_index_1]
        gene_subset_2 = parent_2.genome[split_index_1:split_index_2]
        gene_subset_3 = parent_1.genome[split_index_2:]

        new_genome = gene_subset_1 + gene_subset_2 + gene_subset_3

        child = Individual(self.target_size, genome=new_genome)
        return child

    def mutate(self, population):
        """
        Mutates select individuals from a population.

        Args:
            population (list): A population of individuals.

        """
        num_mutate = int(self.population_mutation_rate * self.population_size)
        mutate_indices = set()

        while len(mutate_indices) < num_mutate:
            selected_index = randint(0, self.population_size - 1)
            mutate_indices.add(selected_index)

        for index in mutate_indices:
            population.individuals[index].mutate_gene()