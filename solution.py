
import numpy as np
import matplotlib.pyplot as plt

def LInpltPoly(x, zero_list, func):

    y = 0

    for i in range(len(zero_list)):

        xi = zero_list[i]
        fxi = func(xi)

        l1 = 1
        l2 = 1

        for j in range(len(zero_list)):

            if i != j:

                xj = zero_list[j]
                l1 = l1 * (x - xj)
                l2 = l2 * (xi - xj)

        li = l1 / l2

        y = y + fxi * li

    return y

def HInpltPoly(x, zero_list, func, func_der):

    h = 0

    for i in range(len(zero_list)):

        xi = zero_list[i]
        yi = func(xi)
        mi = func_der(xi)

        l1 = 1
        l2 = 1
        ld1 = 0

        for j in range(len(zero_list)):

            if i != j:

                xj = zero_list[j]
                l1 = l1 * (x - xj)
                l2 = l2 * (xi - xj)
                ld1 = ld1 + 1 / (xi - xj)

        li = l1 / l2
        ldi = ld1

        ai = (1 - 2 * ldi * (x - xi)) * li * li
        bi = (x - xi) * li * li

        h = h + (yi * ai + mi * bi)

    return h