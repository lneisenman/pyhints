# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals,
                        division, absolute_import)

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt


def peval(x, A, k, theta):
    return A * np.sin((2 * np.pi * k * x) + theta)


def residuals(p, y, x):
    err = y - peval(x, *p)
    return err


def cost(p, y, x):
    err = residuals(p, y, x)
    err_sq = np.square(err)
    return np.sum(err_sq)


if __name__ == '__main__':
    x = np.arange(0, 6e-2, 6e-2 / 30)
    p = A, k, theta = 10, 1.0 / 3e-2, np.pi / 6
    y_true = peval(x, *p)
    y_meas = y_true + 2 * np.random.randn(len(x))

    p0 = [8, 1 / 2.3e-2, np.pi / 3]
    print('p0 =', np.array(p0))

    # use uncontrained slsqp
    fit = opt.minimize(cost, p0, args=(y_meas, x), method='SLSQP')

    if fit.success:
        print('Unconstrained SLSQP fit parameters =', fit.x)
        plt.plot(x, peval(x, *fit.x), x, y_meas, 'o', x, y_true)
        plt.title('SLSQP fit to noisy data without constraints')
        plt.legend(['Fit', 'Noisy', 'True'])
        plt.figure()
    else:
        print('fit failed', fit.message)

    # use contrained slsqp
    bounds = [(5, 15), (20, 50), (0, 2 * np.pi)]
    fit2 = opt.minimize(cost, p0, bounds=bounds, args=(y_meas, x),
                        method='SLSQP')

    if fit2.success:
        print('Constrained SLSQP fit parameters =', fit2.x)
        plt.plot(x, peval(x, *fit2.x), x, y_meas, 'o', x, y_true)
        plt.title('SLSQP fit to noisy data with bounds')
        plt.legend(['Fit', 'Noisy', 'True'])
    else:
        print('constrained fit failed', fit2.message)

    print('True parameters =', np.array([A, k, theta]))
    plt.show()