=======================================
Numpy and Scipy Least Squares Fitting 1
=======================================

Least Squares Fitting
=====================

.. container:: codefile
   
   .. literalinclude:: code/leastsq.py
      :language: py3
      :linenos:


Some Comments:

   * This is my revised version of the least squares demo from the Scipy docs

   * To use `scipy.optimize.leastsq`, you need to create a function to be fit that is called a set of x-values and a set of parameters as shown in line 11. In this case, the fitting function is a sinusoidal function.

   * You then need a function that calculates the residuals corresponding to each value of x. As shown on line 15, this function receives the parameters, the target of the fit and the x-values


Least Squares Fitting with curve_fit
====================================

.. container:: codefile

   .. literalinclude:: code/curve_fit.py
      :language: py3
      :linenos:


Some Comments:

   * The curve_fit function provides a nice wrapper for leastsq

   * Note that we no longer need the residual function


Least Squares Fitting with constraints
======================================

.. container:: codefile
   
   .. literalinclude:: code/slsqp.py
      :language: py3
      :linenos:


Some Comments:

   * This extends the least squares example to demonstrate the use of `scipy.optimize.minimize` and the `SLSQP` algorithm to perform a least squares fit with constraints on the ranges of the parameters

   * Unlike `leastsq`, `minimize` requires you to provide a function that actually calculates the error from the residual. This is implemented here in the cost function defined on line 20.

   * Compare the fits over multiple runs and you should see times when `leastsq` and `SLSQP` without constraints give negative amplitudes for A or shifts > 2pi on the x-axis with theta.

   * You'll also see times when all of the fitting functions give bad fits. Tighter bounds on the parameters may decrease the likelihood of a bad fit but of course, you can't always provide tigher bounds.

