=========================
Numpy and Scipy Trivia #2
=========================

Selecting subsets of an array
=============================

.. code-block:: py3

   In [1]: import numpy as np

   In [2]: test = np.arange(10)

   In [3]: selected = np.nonzero(test < 5)

   In [4]: test[selected]
   Out[4]: array([0, 1, 2, 3, 4])

   In [5]: selected = np.nonzero(np.logical_or(test < 3, test > 7))

   In [6]: test[selected]
   Out[6]: array([0, 1, 2, 8, 9])


Finding indices of particular values
====================================

.. code-block:: numpy

   In [1]: import numpy as np

   In [2]: test = np.arange(10)

   In [3]: test = np.append(test, test)

   In [4]: np.where(test == 5)
   Out[4]: (array([ 5, 15]),)


