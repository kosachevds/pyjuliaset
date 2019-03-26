import math
from PIL import Image


def plot(c_value, max_iteration_count, height=500, width=500):
    r_value = _compute_r(c_value)
    x_min = -r_value
    y_min = -r_value
    x_max = r_value
    y_max = r_value
    x_step = abs(x_min - x_max) / width
    y_step = abs(y_min - y_max) / height

    bitmap = Image.new("RGB", (width, height), "white")
    pixels = bitmap.load()
    for i in range(width):
        x_i = x_min + i * x_step
        for j in range(height):
            y_j = y_min + j * y_step
            z_0 = complex(x_i, y_j)
            count = _count_iterations(z_0, c_value, max_iteration_count, r_value)
            pixels[i, j] = _get_color(count)
    bitmap.show()


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


def _get_color(i):
    return (i << 21) + (i << 10) + i * 8
