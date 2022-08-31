def calculate_ac_a_ratio(ipd, near_deviation, distance_deviation, near_fixation_distance=0.4):
    return ipd + near_fixation_distance * (near_deviation - distance_deviation)
