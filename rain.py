"""Reads history of rainfall at Sunnyside school and determines rain records"""
import re
from datetime import datetime

month_dict = {'JAN' : 1, 'FEB' : 2, 'MAR' : 3, 'APR' : 4, 'MAY' : 5, 'JUN' : 6, 'JUL' : 7, 'AUG' : 8, 'SEP' : 9,
           'OCT' : 10, 'NOV' : 11, 'DEC' : 12}

def read_file_to_list(file_name):
    """Opens rain-data file and creates a list of dates with corresponding rainfall

    :param file_name:
    :return: list of tuples (date, rainfall)
    """
    rainfall_dict = {}
    with open(file_name) as rain_file:
        for line in rain_file.readlines():
            info_match = re.search('\d\d[-]\w{3}[-]\d{4}\s*\d*', line)
            if info_match != None:
                s = info_match.start()
                e = info_match.end()
                rain_info = (line[s:e].split())
                date_string = convert_date_to_std_format(rain_info[0])
                # add reformatted date back into the string
                rain_info[0] = date_string
                rain_info[1] = int(rain_info[1])
                rainfall_dict.update({rain_info[0]:rain_info[1]})
    return rainfall_dict

def convert_date_to_std_format(date_string):
    month_match = re.search('\w{3}', date_string)
    if month_match != None:
        m_s = month_match.start()
        m_e = month_match.end()
        month_str = date_string[m_s:m_e]
    # assigns corresponding number to month (ex> MAR : 3)
    month_num = str(month_dict.get((date_string)[m_s:m_e]))
    year = date_string[-4:]
    day = date_string[:2]
    std_date_string = year + '-' + month_num + '-' + day
    return std_date_string

def day_with_most_rain(rainfall_dict):
    rainfall_tenths = []
    for tenths in rainfall_dict.values():
        rainfall_tenths.append(tenths)
    max_value = max(rainfall_tenths)

    heaviest_rainfall_dates = []
    for date, tenths in rainfall_dict.items():
        if tenths == max_value:
            heaviest_rainfall_dates.append(date)
    max_value = [str(max_value)]
    max_rain_with_dates = max_value + heaviest_rainfall_dates

    return max_rain_with_dates

def year_with_most_rain(rainfall_dict):



def main():

    file_name = 'little_rain.txt'
    rainfall_dict = read_file_to_list(file_name)
    print(rainfall_dict)

    max_rain_with_dates = day_with_most_rain(rainfall_dict)
    if len(max_rain_with_dates) == 2:
        print('The day with the most rainfall on record is ' + max_rain_with_dates[1] +
              ' with ' + max_rain_with_dates[0] + ' tenths of an inch of rain.')
    else:
        print('The days with the most rainfall on record are ', end='')
        for index in max_rain_with_dates[1:]:
            print(index + ', ', end='')
        print(' with ' + max_rain_with_dates[0] + ' tenths of an inch of rain')



if __name__ == '__main__':
    main()