```
Author:      T. Stratton
Start Date:  30-MAR-2025
```

---

# PolyEvolve 2D
This project uses a genetic algorithm to approximate an image.

A target image is provided, then "populations" of candidate images ("individuals") are created and evolved. The "genome" 
of a candidate image is a set of transparent colored polygons. "Genes" are "mutated" by perturbing the vertices and color
of a polygon to a random distance within a set radius of the original value.

### Current Functionality
Candidate images are generated and the most fit from each generation is saved as a PNG. As it still needs to be tuned, 
the results are currently garbage.

### Future Functionality
- a simple GUI
- parameters adjustment
  - set number of generations
  - set population size
  - fix number of polygons
  - fix or select range of number of polygon edges
  - fix color and opacity or set a palette
  - fix opacity
  - allow transparency
  - set background color and opacity
- adaptive mutation rates
- support for different image formats
- fitness measurement using a perceptually uniform color space (CIELAB or Lab, instead of RGB)
- different crossover methods (including multi-parent)
- plotting fitness over time