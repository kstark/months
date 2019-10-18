========
Usage
========

To use months in a project::

    import months

    month = months.Month(2015, 4)
    print(month.full_display)           # April 2015
    print(month.month_abbr)             # Apr
    print(month + 9)                    # 2016-01
    print(month.start_date)             # datetime.date(2015, 4, 1)
    print(month.n_days)                 # 30
    print(month.dates[-1])              # datetime.date(2015, 4, 30)
    print(month.nth(-1))                # datetime.date(2015, 4, 30)
    print(month.to(2015, 5))            # [Month(2015, 4), Month(2015, 5)]
    print(month.distance(month + 3))    # 3
    print(month.gregorian_month_number) # 24172
    print(int(month))                   # 201504
    print(float(month))                 # 201504.0
