import math
from matplotlib import pyplot as pp


def plot(c_value, iteration_count, height=1000, width=1000):
    r_value = _compute_r(c_value)
    x_min = -r_value
    y_min = -r_value
    x_max = r_value
    y_max = r_value
    x_step = abs(x_min - x_max) / width
    y_step = abs(y_min - y_max) / height

    xy_idx = {}
    max_idx = 0
    for i in range(width):
        xy_idx[i] = {}
        x_i = x_min + i * x_step
        for j in range(height):
            y_j = y_min + j * y_step
            z_0 = complex(x_i, y_j)
            z_values = _compute_points(z_0, c_value, iteration_count, r_value)
            idx = len(z_values) - 1
            max_idx = max(max_idx, idx)
            xy_idx[i][j] = idx

    for i in range(width):
        x_i = x_min + i * x_step
        for j in range(height):
            y_j = y_min + j * y_step
            z_ij = complex(x_i, y_j)
            if abs(z_ij) / r_value > 1:
                pp.plot(x_i, y_j)
    pp.show()

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


def _get_color(i):
    return (i << 21) + (i << 10) + i * 8
