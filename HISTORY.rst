.. :changelog:

History
-------

2.0.0 (2019-10-18)
---------------------

* Thanks to nolanbconaway for their contributions!
* New methods to handle relations between months:
   * ``month.to(other)`` for generating intervals of months.
   * ``month.distance(other)`` for computing distance between months.
* New methods for month date info
   * ``month.n_days`` to return the number of days in the month.
   * ``month.dates`` to return a list of all days in the month.
   * ``month.nth(day)`` to return a specific day in the month.
* ``__int__`` and ``__float__`` methods added.
   * Also a ``month.gregorian_month_number`` method to compute number of months
     since year 0.

1.1.0 (2019-10-18)
---------------------

* Support up to Python 3.8, drop explicit support for 2.6/3.2/3.3
* Raise TypeError on invalid addition/subtraction instead of ValueError

1.0.0 (2015-04-13)
---------------------

* Documentation added
* 2.6 support added
* Tests for bad math added

0.1.0 (2015-04-13)
---------------------

* First release on PyPI.
