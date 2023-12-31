import jdatetime


def datetime_to_number(datetime: jdatetime, to_what: str):
    if to_what == 'month':
        month_number = datetime.month
        return month_number
    elif to_what == 'week':
        week_number = datetime.isocalendar()[1]
        return int(week_number)
    elif to_what == 'day':
        day_number = int(datetime.strftime('%j'))
        return day_number
    else:
        return print('datetime_to_number. err: to_what is undefined')


def day_calculator(date: jdatetime):
    x = jdatetime.datetime.now()
    if date.month <= 6:
        day = (date.month - 1) * 31 + date.day
    else:
        day = (date.month - 1) * 30 + date.day

    return day

#
# def week_calculator(date_from: jdatetime, date_to: jdatetime):
#     week_from = int((day_calculator(date_from, date_to)[0][1] / 7) + 1)
#     week_to = int((day_calculator(date_from, date_to)[1][1] / 7) + 1)
#     duration = week_to - week_from + 1
#     return [week_from - 1, week_from], [week_to - 1, week_to], duration

