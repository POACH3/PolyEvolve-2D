"""
Orchestrates the genetic algorithm, supporting future MVC structure.
"""

import matplotlib.pyplot as plt

def plot(gen_alg):

    # add other metrics (individual fitness, average fitness, etc)
    x_axis, max_fitness_data, min_fitness_data, avg_fitness_data = [], [], [], []

    for gen in range(gen_alg.num_generations):
        for ind in range(gen_alg.population_size):
            fitnesses = [ind.fitness for ind in gen_alg.generations[gen].population]
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
    """
    Runs the genetic algorithm.
    
    Saves files and displays the fitness plot.
    """

    METHOD = "V2"

    if METHOD == "V1":
        from version_1 import GeneticAlgorithm, ImageRenderer, Population, Individual, Polygon

        renderer = ImageRenderer()
        target = renderer.load_image("./simplest_smoll.png")
        # target = renderer.load_image("./simple_smoll.png")
        # target = renderer.load_image("./majesticUnicorn_smoll.png")

        gen_alg = GeneticAlgorithm(target)
        gen_alg.evolve()
        plot(gen_alg)

    elif METHOD == "V2":
        from version_2.genetic_algorithm import GeneticAlgorithm
        from version_2.image_renderer import ImageRenderer

        renderer = ImageRenderer()
        #target = renderer.load_image("./simplest_smoll.png")
        #target = renderer.load_image("./simple_smoll.png")
        target = renderer.load_image("./majesticUnicorn_smoll.png")

        gen_alg = GeneticAlgorithm(target)
        gen_alg.evolve()
        plot(gen_alg)

    else:
        raise ValueError("Unknown method")