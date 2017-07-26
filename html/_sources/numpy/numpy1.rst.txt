=========================
Numpy and Scipy Trivia #1
=========================

standard imports
================

.. code-block:: py3

   import numpy as np
   import scipy as sp
   import matplotlib.pyplot as plt


np.show_config
==============

Use the command ``np.show_config()`` to see how numpy was compiled and what libraries were used

sp.show_config
==============

Use the command ``sp.show_config()`` to see how scipy was compiled and what libraries were used

Creating numpy arrays
=====================

The command ``np.asarray()`` can be used to create numpy arrays out of any list like data. It can also be used to change the data type (e.g. from float to int) by including a dtype parameter as in ``int_array = np.asarray(float_array, dtype=np.int)``

Reversing a numpy array
=======================

.. code-block:: numpy

   In [1]: import numpy as np

   In [2]: forward = np.arange(5)

   In [3]: forward
   Out[3]: array([0, 1, 2, 3, 4])

   In [4]: backward = forward[::-1]

   In [5]: backward2 = forward[::-1].copy()

   In [6]: backward
   Out[6]: array([4, 3, 2, 1, 0])

   In [7]: backward2
   Out[7]: array([4, 3, 2, 1, 0])

   In [8]: forward[1] = 6

   In [9]: backward
   Out[9]: array([4, 3, 2, 6, 0])

   In [10]: backward2
   Out[10]: array([4, 3, 2, 1, 0])

