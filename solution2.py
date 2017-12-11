
import numpy as np

def ChebyshevZeros(a, b, n):

    zero_list = []

    for i in range(0, n):

         zero = np.cos((2 * i + 1) * np.pi / (2 * n))

         new_zero = (a + b) / 2 + (b - a) * zero / 2

         zero_list.append(new_zero)

    return zero_list