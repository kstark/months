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

    def test_sub(self):
        self.assertEqual(self.month - 1, Month(2015, 3))

    def test_sub_rollover(self):
        self.assertEqual(self.month - 4, Month(2014, 12))

    def test_start_date(self):
        self.assertEqual(self.month.start_date, self.date.replace(day=1))

    def test_end_date(self):
        self.assertEqual(self.month.end_date, self.date.replace(day=30))

    def test_range(self):
        self.assertEqual(
            self.month.range,
            (self.date.replace(day=1), self.date.replace(day=30)))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
