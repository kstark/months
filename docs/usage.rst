========
Usage
========

To use months in a project::

    import months

    month = months.Month(2015, 4)
    print(month.full_display)  # April 2015
    print(month.month_abbr     # Apr
    print(month + 9)           # 2016-01
    print(month.start_date)    # datetime.date(2015, 4, 1)
