# PolyEvolve 2D Version 2
This method uses a more iterative genetic algorithm to approximate an image.

It tests new candidates, but only retains them if they are an improvement over the current candidate.

### Current Functionality
Candidate images are generated and the most fit from each generation is saved as a PNG.
Fitness over the generations is plotted.

### Notes
 - maybe initialize genes to the background color
 - maybe start with no genes and only "evolve" a new one if progress stagnates
 - correct polygons so they can only be simple