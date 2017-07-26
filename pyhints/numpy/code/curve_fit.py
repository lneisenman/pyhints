# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals,
                        division, absolute_import)

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt


def peval(x, A, k, theta):
    return A * np.sin((2 * np.pi * k * x) + theta)


if __name__ == '__main__':
    x = np.arange(0, 6e-2, 6e-2 / 30)
    p = A, k, theta = 10, 1.0 / 3e-2, np.pi / 6
    y_true = peval(x, *p)
    y_meas = y_true + 2 * np.random.randn(len(x))

    p0 = [8, 1 / 2.3e-2, np.pi / 3]
    print('Initial guess for A, k , theta =', np.array(p0))

    popt, pcov = opt.curve_fit(peval, x, y_meas, p0)
    print('Best fit values of A, k, theta =', popt)
    print('True values of A, k, theta =', np.array([A, k, theta]))

    plt.plot(x, peval(x, *popt), x, y_meas, 'o', x, y_true)
    plt.title('Least-squares fit to noisy data')
    plt.legend(['Fit', 'Noisy', 'True'])
    plt.show()