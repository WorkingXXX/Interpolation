
import numpy as np

def RangeIndex(x, num_range):

    for i in range(0, len(num_range)-1):

        if (num_range[i] <= x <= num_range[i+1]) : return i

def PLinearInplt(x, zero_list, func):

    result = []

    for xi in x:

        k = RangeIndex(xi, zero_list)

        x0 = zero_list[k]
        f0 = func(x0)
        x1 = zero_list[k + 1]
        f1 = func(x1)

        l0 = (xi - x1) / (x0 - x1)
        l1 = (xi - x0) / (x1 - x0)

        result.append(f0 * l0 + f1 * l1)

    return result


def THInpltPoly(x, zero_list, func, func_der):

    result = []

    for xi in x:

        k = RangeIndex(xi, zero_list)
        xk = zero_list[k]

        fk = func(xk)
        fdk = func_der(xk)

        xk_1 = zero_list[k + 1]
        fk_1 = func(xk_1)
        fdk_1 = func_der(xk_1)

        ak = (1 + 2 * (xi - xk) / (xk_1 - xk)) * ((xi - xk_1) / (xk - xk_1)) * ((xi - xk_1) / (xk - xk_1))
        ak_1 = (1 + 2 * (xi - xk_1) / (xk - xk_1)) * ((xi - xk) / (xk_1 - xk)) * ((xi - xk) / (xk_1 - xk))
        bk = (xi - xk) * ((xi - xk_1) / (xk - xk_1)) * ((xi - xk_1) / (xk - xk_1))
        bk_1 = (xi - xk_1) * ((xi - xk) / (xk_1 - xk)) * ((xi - xk) / (xk_1 - xk))

        result.append(fk * ak + fk_1 * ak_1 + fdk * bk + fdk_1 * bk_1)

    return result

