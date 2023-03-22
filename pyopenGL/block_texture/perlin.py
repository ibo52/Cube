# create a Perlin texture in 2D
#REFERENCE: https://iq.opengenus.org/perlin-noise/

import numpy as np
from matplotlib import pyplot as plot

def gradient(c, x: int, y: int):
    vectors = np.array([[0, 1], [0, -1], [1, 0], [-1, 0]])

    gradient_co = vectors[c % 4]
    return gradient_co[:, :, 0] * x + gradient_co[:, :, 1] * y
def fade(f):
    return 6 * f ** 5 - 15 * f ** 4 + 10 * f ** 3


def lerp(a, b, x):
    "linear interpolation i.e dot product"
    return a + x * (b - a)


def perlin(x: float, y: float, seed=0):
    np.random.seed(seed)

    permutation_table = np.arange(256, dtype=int)
    np.random.shuffle(permutation_table)

    permutation_table = np.stack([permutation_table, permutation_table]).flatten()

    xi = x.astype(int)
    yi = y.astype(int)

    sx = x - xi
    sy = y - yi

    xf, yf = fade(sx), fade(sy)

    n00 = gradient(permutation_table[permutation_table[xi] + yi], sx, sy)
    n01 = gradient(permutation_table[permutation_table[xi] + yi + 1], sx, sy - 1)
    n10 = gradient(permutation_table[permutation_table[xi + 1] + yi], sx - 1, sy)
    n11 = gradient(permutation_table[permutation_table[xi + 1] + yi + 1], sx - 1, sy - 1)

    x1 = lerp(n00, n10, xf)
    x2 = lerp(n01, n11, xf)
    return lerp(x1, x2, yf)

if __name__=="__main__":
    # create evenly spaced out numbers in a specified interval
    lin_array = np.linspace(0, 15, 16, endpoint=False)

    # create grid using linear 1d arrays
    x, y = np.meshgrid(lin_array, lin_array)

    # generate graph
    plot.imshow(perlin(x,y,seed=2), origin='upper')

    plot.show()