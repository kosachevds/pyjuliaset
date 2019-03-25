import math


def plot(c_value, iteration_count):
    pass


def _compute_points(z_0, c_value, iteration_count, r_value):
    result = [z_0]
    for _ in range(iteration_count):
        previous = result[-1]
        if abs(previous) > r_value > 0:
            break
        result.append(previous * previous + c_value)
    return result


def _compute_r(c_value):
    return (1 + math.sqrt(1 + 4 * abs(c_value))) / 2
