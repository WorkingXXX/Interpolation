
import numpy as np
import matplotlib.pyplot as plt
import solution as s1
import solution2 as s2
import solution3 as s3

def func(x) : return 1 / (1 + x * x)
def func_der(x) : return -(2 * x / ((1 + x * x) * (1 + x * x)))
def average_error(x1, x2):
    ae = 0
    for i in range(0, len(x1)):
        ae = ae + np.fabs(x1[i] - x2[i])
    return ae / len(x1)


zeros = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
x_range = np.arange(-5, 5, 0.1)
yf = func(x_range)

fig11 = plt.figure('Solution1-Lagrange')
yl1 = s1.LInpltPoly(x_range, zeros, func)
ae1 = average_error(yl1, yf)
plt.text(-2, 1.5, 'AverageError = %f' % ae1)
plt.plot(x_range, yl1)
plt.plot(x_range, yf)
fig12 = plt.figure('Solution1-Hermite')
yh1 = s1.HInpltPoly(x_range, zeros, func, func_der)
ae2 = average_error(yh1, yf)
plt.text(-2, 3, 'AverageError = %f' % ae2)
plt.plot(x_range, yh1)
plt.plot(x_range, yf)

fig2 = plt.figure('Solution2-Chebyshev')
yl2 = s1.LInpltPoly(x_range, s2.ChebyshevZeros(-5, 5, 11), func)
ae3 = average_error(yl2, yf)
plt.text(-5.0, 0.7, 'AverageError = %f' % ae3)
plt.plot(x_range, yl2)
plt.plot(x_range, yf)

fig31 = plt.figure('Solution3-PLinearInplt')
ypl = s3.PLinearInplt(x_range, zeros, func)
ae4= average_error(ypl, yf)
plt.text(-4.8, 0.7, 'AverageError = %f' % ae4)
plt.plot(x_range, ypl)
plt.plot(x_range, yf)
fig32 = plt.figure('Solution3-PTHermiteInplt')
ypth = s3.THInpltPoly(x_range, zeros, func, func_der)
ae5= average_error(ypth, yf)
plt.text(-4.8, 0.7, 'AverageError = %f' % ae5)
plt.plot(x_range, ypth)
plt.plot(x_range, yf)

plt.show()