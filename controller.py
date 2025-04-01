"""
Orchestrates the genetic algorithm, supporting future MVC structure.
"""

from genetic_algorithm import GeneticAlgorithm
from image_renderer import ImageRenderer
from individual import Individual


class Controller:
    def __init__(self, target_path, population_size, num_generations):
        # Initialize parameters
        self.target_path = target_path
        self.population_size = population_size
        self.num_generations = num_generations

        # Example: load target image and initialize population
        self.target_image = self.load_target_image(target_path)
        self.population = self.initialize_population(population_size)

    def load_target_image(self, path):
        # Placeholder: implement image loading logic (e.g., using Pillow)
        print(f"Loading target image from: {path}")
        return None  # Replace with actual image object

    def run(self):
        # Main evolution loop
        for gen in range(self.generations):
            print(f"Generation {gen}")
            self.evaluate_population()
            self.evolve_population()
            # Optionally: Save best individual image, log stats, etc.
        print("Evolution complete")


if __name__ == "__main__":

    #controller = Controller("target.png", population_size=50, num_generations=1000)
    #controller.run()

    renderer = ImageRenderer()
    target = renderer.load_image("./majesticUnicorn_smoll.png")
    #height, width = target.size
    #renderer.show_image(target)

    #individual = Individual((500,500), num_genes=10)
    #test_im = renderer.create_image(individual)
    #renderer.save_image(test_im, "./polyevolve_images/test.png")

    gen_alg = GeneticAlgorithm(target)
    gen_alg.evolve()

    # save files
    # log data
    # display final image
