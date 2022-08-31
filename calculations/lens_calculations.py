import numpy as np

def radius_of_curvature_to_power(radius):
    return 337.5 / radius

def focal_power(n1, n2, radius1, radius2):
    return (n2 - n1) * (1 / radius1 - 1 / radius2)
