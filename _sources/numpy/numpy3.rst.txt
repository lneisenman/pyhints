==========================
Numpy and Scipy Statistics
==========================

Basic Stats
===========

Mean: ``np.average()`` or ``np.mean()``

Standard Deviation: ``np.std()``

Variance: ``np.var()``

Maximim: ``np.max()``

Minimum: ``np.min()``

Sum: ``np.sum()``

Cumulative Sum: ``np.cumsum()``


t-tests
=======

Computing t-tests requires importing Scipy.stats (``from scipy import stats``)

For a one sample t-test (two-tailed): ``t_stat, p_value = stats.ttest_1samp(values, expected_mean)``

For a two sample t-test (two-tailed): ``t_stat, p_value = stats.ttest_ind(values1, values2)``

For a two sample repeated measures t-test (two-tailed): ``t_stat, p_value = stats.ttest_rel(values1, values2)``


Other tests
===========

For other tests, try the `Scipy Statistics <http://docs.scipy.org/doc/scipy/reference/stats.html>`_ docs.
