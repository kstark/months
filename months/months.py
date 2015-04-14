# -*- coding: utf-8 -*-
from collections import namedtuple
import calendar
import datetime


def __utctoday():
    """ Returns today's date in UTC time """
    return datetime.datetime.utcnow().date()


class Month(namedtuple('Month', ['year', 'month'])):
    """
    Represents a specific month of a year

    Provides various utilites for generating, manipulating, and displaying
    months.
    """
    def __repr__(self):
        return "%s(%d, %d)" % (self.__class__.__name__, self.year, self.month)

    def __str__(self):
        return self.start_date.strftime("%Y-%m")

    @property
    def month_name(self):
        """
        The calendar name of the month.

        >>> Month(2015, 4).month_name
        'April'
        """
        return calendar.month_name[self.month]

    @property
    def month_abbr(self):
        """
        The abbreviated calendar name of the month.

        >>> Month(2015, 4).month_abbr
        'Apr'
        """
        return calendar.month_abbr[self.month]

    @property
    def full_display(self):
        """
        The calendar name of the month along with the year

        >>> Month(2015, 4).full_display
        'April 2015'
        """
        return "{} {}".format(self.month_name, self.year)

    @property
    def abbr_display(self):
        """
        The abbreviated calendar name of the month along with the year

        >>> Month(2015, 4).full_display
        'Apr 2015'
        """
        return "{} {}".format(self.month_abbr, self.year)

    @classmethod
    def from_date(cls, date):
        """
        Returns a Month instance from the given datetime.date or
        datetime.datetime object
        """
        try:
            date = date.date()
        except AttributeError:
            pass
        return cls(date.year, date.month)

    @classmethod
    def from_today(cls):
        """
        Returns a Month instance from today's date (local time)
        """
        return cls.from_date(datetime.date.today())

    @classmethod
    def from_utc_today(cls):
        """
        Returns a Month instance from today's date (UTC time)
        """
        return cls.from_date(__utctoday())

    def __add__(self, other):
        """
        Offsets a number of months into the future

        >>> Month(2015, 4) + 9
        Month(2016, 1)
        """
        if not isinstance(other, int):
            raise ValueError("Only ints can be added to months")

        year_change, month = divmod(self.month + other - 1, 12)
        return type(self)(self.year + year_change, month + 1)

    def __sub__(self, other):
        """
        Offsets a number of months into the past

        >>> Month(2015, 4) - 9
        Month(2014, 7)
        """
        if not isinstance(other, int):
            raise ValueError("Only ints can be added to months")

        return self + (-other)

    @property
    def start_date(self):
        """ Returns a datetime.date object for the first day of the month """
        return datetime.date(self.year, self.month, 1)

    @property
    def end_date(self):
        """ Returns a datetime.date object for the last day of the month """
        return (self + 1).start_date - datetime.timedelta(1)

    @property
    def range(self):
        """ Returns a tuple of the first and last days of the month """
        return (self.start_date, self.end_date)
