# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals,
                        division, absolute_import)

import numpy as np
import lmfit as lmf
import matplotlib.pyplot as plt


def peval(x, A, k, theta):
    return A * np.sin((2 * np.pi * k * x) + theta)


def print_params(params):
    for name, param in params.items():
        print(name, "=", param.value)


if __name__ == '__main__':
    peval_model = lmf.Model(peval)
    x = np.arange(0, 6e-2, 6e-2 / 30)
    p = peval_model.make_params(A=10, k=1/3.2e-2, theta=np.pi/6)
    y_true = peval_model.eval(x=x, params=p)
    y_meas = y_true + 2 * np.random.randn(len(x))

    p0 = lmf.Parameters()
    p0.add('A', value=8, min=5, max=15)
    p0.add('k', value=1/2.3e-2, min=20, max=60)
    p0.add('theta', value=np.pi/3, min=0, max=2*np.pi)

    print("initial guess")
    print_params(p0)

    fit = peval_model.fit(data=y_meas, params=p0, x=x)
    if fit.success:
        print()
        print("fitted parameters")
        print(fit.best_values)
        print()
    else:
        print('fit failed', fit.message)

    print("True parameters")
    print_params(p)

    plt.plot(x, peval(x, **fit.best_values), x, y_meas, 'o', x, y_true)
    plt.title('lmfit Least-squares fit to noisy data')
    plt.legend(['Fit', 'Noisy', 'True'])
    plt.figure()
    fit.plot_fit()
    plt.show()
