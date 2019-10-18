#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_months
----------------------------------

Tests for `months` module.
"""

import os
import sys
import datetime
import unittest

sys.path.append(os.path.join('.', 'months'))
sys.path.append(os.path.join('..', 'months'))

from months import Month


class TestMonths(unittest.TestCase):

    def setUp(self):
        self.datetime = datetime.datetime(2015, 4, 15)
        self.date = self.datetime.date()
        self.month = Month(2015, 4)

    def test_repr(self):
        self.assertEqual(repr(self.month), 'Month(2015, 4)')

    def test_str(self):
        self.assertEqual(str(self.month), '2015-04')

    def test_int(self):
        self.assertEqual(int(self.month), 201504)

    def test_float(self):
        self.assertEqual(float(self.month), 201504.0)

    def test_month_name(self):
        self.assertEqual(self.month.month_name, 'April')

    def test_month_abbr(self):
        self.assertEqual(self.month.month_abbr, 'Apr')

    def test_full_display(self):
        self.assertEqual(self.month.full_display, 'April 2015')

    def test_abbr_display(self):
        self.assertEqual(self.month.abbr_display, 'Apr 2015')

    def test_from_datetime(self):
        self.assertEqual(self.month, Month.from_date(self.datetime))

    def test_from_date(self):
        self.assertEqual(self.month, Month.from_date(self.date))

    def test_add(self):
        self.assertEqual(self.month + 1, Month(2015, 5))

    def test_add_rollover(self):
        self.assertEqual(self.month + 9, Month(2016, 1))

    def test_add_raises(self):
        self.assertRaises(TypeError, self.month.__add__, 'not_an_int')

    def test_sub(self):
        self.assertEqual(self.month - 1, Month(2015, 3))

    def test_sub_rollover(self):
        self.assertEqual(self.month - 4, Month(2014, 12))

    def test_sub_raises(self):
        self.assertRaises(TypeError, self.month.__sub__, 'not_an_int')

    def test_start_date(self):
        self.assertEqual(self.month.start_date, self.date.replace(day=1))

    def test_end_date(self):
        self.assertEqual(self.month.end_date, self.date.replace(day=30))

    def test_range(self):
        self.assertEqual(
            self.month.range,
            (self.date.replace(day=1), self.date.replace(day=30)))

    def test_dates(self):
        self.assertEqual(self.month.dates[0], self.month.start_date)

    def test_n_days(self):
        self.assertEqual(self.month.n_days, len(self.month.dates))

    def test_nth(self):
        self.assertEqual(self.month.nth(-1), self.month.end_date)

    def test_to(self):

        other = self.month-1
        self.assertEqual(self.month.to(other), [self.month, other])

        other = (2004, 5)
        self.assertEqual(self.month.to(*other)[-1], Month(*other))
        self.assertEqual(self.month.to(other)[-1], Month(*other))

        other = datetime.date(2004, 5, 10)
        self.assertEqual(self.month.to(other)[-1], Month.from_date(other))

    def test_distance(self):

        d = 10
        self.assertEqual(self.month.distance(self.month + d), d)
        self.assertEqual(self.month.distance(self.month - d), d)

        other_tup = ((self.month - d).year, (self.month - d).month)
        self.assertEqual(self.month.distance(*other_tup), d)
        self.assertEqual(self.month.distance(other_tup), d)

        other_dt = (self.month - d).nth(5)
        self.assertEqual(self.month.distance(other_dt), d)

    def test_gregorian_number(self):
        self.assertEqual(Month(1, 1).gregorian_month_number, 1)
        self.assertEqual(Month(-1, 2).gregorian_month_number, -2)
        self.assertEqual(Month(2, 2).gregorian_month_number, 14)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
