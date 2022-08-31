def astigmatism_fan_block_test(best_sphere, approx_cylinder_power, visual_acuity):
    plus_power = best_sphere + approx_cylinder_power / 2
    return plus_power

def calculate_cylinder_power(clear_line_power, added_power):
    return clear_line_power + added_power
