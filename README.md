```
Author:      T. Stratton
Start Date:  30-MAR-2025
```

---

# PolyEvolve 2D
Inspired by Roger Alsing's [Evolution of Mona Lisa](https://rogerjohansson.blog/2008/12/07/genetic-programming-evolution-of-mona-lisa/), this project uses a genetic algorithm to approximate an image using a few polygons.


### Notes:
The [first approach](https://github.com/POACH3/PolyEvolve-2D/tree/main/version_1) has been abandoned (for now) due to lack of convergence to a good approximation, despite significant simplification of target images and parameter experimentation.


The results of the [second approach](https://github.com/POACH3/PolyEvolve-2D/tree/main/version_2) are crude, but a significant improvement over version 1.

##### Possible Future Features
- a simple GUI
- parameter adjustment
  - set number of generations
  - set population size
  - fix number of polygons
  - fix or select range of number of polygon edges
  - fix color and opacity or set a palette
  - fix opacity
  - allow transparency
  - set background color and opacity
- circles
- parallelize via multiprocessing
  - fitness measurement
  - clone mutation