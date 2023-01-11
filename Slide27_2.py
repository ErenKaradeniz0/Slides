def days_till(start_month, start_day, stop_month, stop_day):
    months = (('january', 31), ("february", 28), ('march', 31), ("april", 30), ('may', 31), ("june", 30),
              ('july', 31), ('august', 31), ("september", 30), ("october", 31), ("november", 30), ("december", 31))

    if start_month.lower() == stop_month.lower() and stop_day >= start_day:
        return stop_day-start_day

    days = 0
    for i in range(0, len(months)):
        mont = months[i]
        if mont[i] == start_month.lower():
            days = mont[1]-start_day
            i += 1
            while months[i % 12][0] != stop_month.lower():
                days += months[i % 12][1]
                i += 1
        days += stop_day
        return days


print(days_till("January", 1, "February", 10))
