"""
Fitness evaluation functionality used by the genetic algorithm.
It will receive an approximation image and a target image, then measure the
RGB distance between the two. MSE to start, but eventually will account for
curved color space.
"""