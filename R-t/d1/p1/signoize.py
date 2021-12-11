"""Python3 program creates a 2000px square image from scratch that depicts a chaotic fractal.
"""

import random
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    """Main function.
    """
    # Create a 2000x2000 pixel image.
    img = np.zeros((2000, 2000, 3), dtype=np.uint8)

    # Set the seed for the random number generator.
    random.seed(1)

    # Create the fractal.
    for i in range(2000):
        for j in range(2000):
            x = i / 2000
            y = j / 2000
            img[i, j] = get_color(x, y)

    # Save the image.
    plt.imsave('fractal.png', img)

def get_color(x, y):
    """Returns the color of the pixel at the given coordinates.
    """
    # Get the number of iterations.
    n = get_iterations(x, y)

    # Return the color.
    return (n % 255, n % 255, n % 255)

def get_iterations(x, y):
    """Returns the number of iterations for the given coordinates.
    """
    # Initialize the number of iterations.
    n = 0

    # Iterate until the number of iterations exceeds the maximum.
    while n < 255:
        # Get the coordinates of the next point.
        x_next = x * x - y * y + 0.285
        y_next = x * y * 2 + 0.01

        # Check if the point is outside the Mandelbrot set.
        if x_next * x_next + y_next * y_next > 100:
            break

        # Update the coordinates.
        x = x_next
        y = y_next

        # Increment the number of iterations.
        n += 1

    # Return the number of iterations.
    return n

if __name__ == '__main__':
    main()