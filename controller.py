"""
Orchestrates the genetic algorithm, supporting future MVC structure.
"""

import matplotlib.pyplot as plt
from genetic_algorithm import GeneticAlgorithm
from image_renderer import ImageRenderer

def plot(gen_alg):

    # add other metrics (individual fitness, average fitness, etc)
    x_axis, max_fitness_data, min_fitness_data, avg_fitness_data = [], [], [], []

    for gen in range(gen_alg.num_generations):
        for individual in range(gen_alg.population_size):
            fitnesses = [individual.fitness for individual in gen_alg.generations[gen].individuals]
            max_fit = max(fitnesses)
            min_fit = min(fitnesses)
            avg_fit = sum(fitnesses) / gen_alg.population_size
            x_axis.append(gen)
            max_fitness_data.append(max_fit)
            min_fitness_data.append(min_fit)
            avg_fitness_data.append(avg_fit)

    fig, ax = plt.subplots()
    ax.set_xlabel("Generation")
    ax.set_ylabel("Fitness")
    ax.set_title("Fitness Over Generations")
    ax.plot(x_axis, max_fitness_data, "r-", label="Max Fitness")
    ax.plot(x_axis, min_fitness_data, "g-", label="Min Fitness")
    ax.plot(x_axis, avg_fitness_data, "b-", label="Avg Fitness")
    ax.legend()
    plt.show()

if __name__ == "__main__":

    renderer = ImageRenderer()
    target = renderer.load_image("./simplest_smoll.png")
    #target = renderer.load_image("./simple_smoll.png")
    #target = renderer.load_image("./majesticUnicorn_smoll.png")

    gen_alg = GeneticAlgorithm(target)
    gen_alg.evolve()
    plot(gen_alg)

    # save files
    # log data
    # display final image
