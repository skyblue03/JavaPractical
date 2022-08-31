import numpy as np

def prismatic_effect_power(cylinder, axis):
    return cylinder * np.sin(np.radians(2 * axis))
