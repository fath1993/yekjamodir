import jdatetime


def persian_date_word_generator(date_in_format_01_01_1398):
    persian_date = str(date_in_format_01_01_1398)
    persian_date = persian_date.replace('-', ' ')
    persian_date = persian_date.split()
    persian_date_day = persian_date[2]
    persian_date_month = persian_date[1]
    persian_date_year = persian_date[0]

    if persian_date_day == '01':
        persian_date_day = 'یکم'
    elif persian_date_day == '02':
        persian_date_day = 'دوم'
    elif persian_date_day == '03':
        persian_date_day = 'سوم'
    elif persian_date_day == '04':
        persian_date_day = 'چهارم'
    elif persian_date_day == '05':
        persian_date_day = 'پنجم'
    elif persian_date_day == '06':
        persian_date_day = 'ششم'
    elif persian_date_day == '07':
        persian_date_day = 'هفتم'
    elif persian_date_day == '08':
        persian_date_day = ' هشتم'
    elif persian_date_day == '09':
        persian_date_day = 'نهم'
    elif persian_date_day == '10':
        persian_date_day = 'دهم'
    elif persian_date_day == '11':
        persian_date_day = 'یازدهم'
    elif persian_date_day == '12':
        persian_date_day = 'دوازدهم'
    elif persian_date_day == '13':
        persian_date_day = 'سیزدهم'
    elif persian_date_day == '14':
        persian_date_day = 'چهاردهم'
    elif persian_date_day == '15':
        persian_date_day = 'پانزدهم'
    elif persian_date_day == '16':
        persian_date_day = 'شانزدهم'
    elif persian_date_day == '17':
        persian_date_day = 'هفدهم'
    elif persian_date_day == '18':
        persian_date_day = 'هجدهم'
    elif persian_date_day == '19':
        persian_date_day = 'نوزدهم'
    elif persian_date_day == '20':
        persian_date_day = 'بیستم'
    elif persian_date_day == '21':
        persian_date_day = 'بیست و یکم'
    elif persian_date_day == '22':
        persian_date_day = 'بیست و دوم'
    elif persian_date_day == '23':
        persian_date_day = 'بیست و سوم'
    elif persian_date_day == '24':
        persian_date_day = 'بیست و چهارم'
    elif persian_date_day == '25':
        persian_date_day = 'بیست و پنجم'
    elif persian_date_day == '26':
        persian_date_day = 'بیست و ششم'
    elif persian_date_day == '27':
        persian_date_day = 'بیست و هفتم'
    elif persian_date_day == '28':
        persian_date_day = 'بیست و هشتم'
    elif persian_date_day == '29':
        persian_date_day = 'بیست و نهم'
    elif persian_date_day == '30':
        persian_date_day = 'سی ام'
    elif persian_date_day == '31':
        persian_date_day = 'سی و یکم'
    else:
        persian_date_day = ''

    if persian_date_month == '01':
        persian_date_month = 'فروردین'
    elif persian_date_month == '02':
        persian_date_month = 'اردیبهشت'
    elif persian_date_month == '03':
        persian_date_month = 'خرداد'
    elif persian_date_month == '04':
        persian_date_month = 'تیر'
    elif persian_date_month == '05':
        persian_date_month = 'مرداد'
    elif persian_date_month == '06':
        persian_date_month = 'شهریور'
    elif persian_date_month == '07':
        persian_date_month = 'مهر'
    elif persian_date_month == '08':
        persian_date_month = 'آبان'
    elif persian_date_month == '09':
        persian_date_month = 'آذر'
    elif persian_date_month == '10':
        persian_date_month = 'دی'
    elif persian_date_month == '11':
        persian_date_month = 'بهمن'
    elif persian_date_month == '12':
        persian_date_month = 'اسفند'
    else:
        persian_date_month = ''

    persian_date_year = 'سال ' + persian_date_year

    final_date_in_word = persian_date_day + " " + persian_date_month + " " + persian_date_year
    return final_date_in_word



def convert_datetime_to_second(date_time_field):
    date_time_field_hour = int(date_time_field.time().hour)
    date_time_field_minute = int(date_time_field.time().minute)
    date_time_field_seconds = int(date_time_field.time().second)
    return date_time_field_hour * 3600 + date_time_field_minute * 60 + date_time_field_seconds


