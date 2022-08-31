def astigmatism_fan_block_test(best_sphere, approx_cylinder_power):
    return best_sphere + approx_cylinder_power / 2

def calculate_cylinder_power(clear_line_power, added_power):
    return clear_line_power + added_power
