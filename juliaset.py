import math
from PIL import Image
import numpy as np


def plot(c_value, max_iteration_count, height=500, width=500):
    r_value = _compute_r(c_value)
    x_list = np.linspace(-r_value, r_value, width)
    y_list = np.linspace(-r_value, r_value, height)

    bitmap = Image.new("RGB", (width, height), "white")
    pixels = bitmap.load()
    for i, x_i in enumerate(x_list):
        for j, y_j in enumerate(y_list):
            z_ij = complex(x_i, y_j)
            count = _count_iterations(z_ij, c_value, max_iteration_count, r_value)
            pixels[i, j] = _get_color(count, max_iteration_count, abs(z_ij) / r_value)
    bitmap.save("temp.bmp")


def _count_iterations(z_0, c_value, iteration_count, r_value):
    count = 0
    current_value = z_0
    for _ in range(iteration_count):
        if abs(current_value) > r_value > 0:
            break
        current_value = current_value ** 2 + c_value
        count += 1
    return count


def _compute_r(c_value):
    return (1 + math.sqrt(1 + 4 * abs(c_value))) / 2


def _get_color(count, max_count, z_to_r_ratio):
    count_ratio = count / max_count
    return (
        int(255 * count_ratio),
        int(255 * (1 - count_ratio)),
        int(255 * min(1, z_to_r_ratio))

    )
