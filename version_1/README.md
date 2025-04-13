# PolyEvolve 2D Version 1

---
This method uses a more traditional genetic algorithm to approximate an image.

A target image is provided, then set ("population") of candidate images ("individuals") are created and evolved. The "genome" 
of a candidate image is a set of transparent colored polygons. "Genes" are "mutated" by perturbing the vertices and color
of a polygon to a random distance within a set radius of the original value.

### Current Functionality
Candidate images are generated and the most fit from each generation is saved as a PNG.
Fitness over the generations is plotted.

As the results are garbage, this approach has been abandoned.

### Possible Future Functionality
- adaptive mutation rates
- support for different image formats
- fitness measurement using a perceptually uniform color space (CIELAB or Lab, instead of RGB)
- different crossover methods (including multi-parent)