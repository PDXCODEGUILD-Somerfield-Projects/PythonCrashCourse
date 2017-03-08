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
                month_match = re.search('\w{3}', rain_info[0])
                if month_match != None:
                    m_s = month_match.start()
                    m_e = month_match.end()
                # assigns corresponding number to month (ex> MAR : 3)
                month = month_dict.get((rain_info[0])[m_s:m_e])
                # add month 'number' back into the string

                rain_info = [r.replace(('\w{3}', month)) for r in rain_info]
                #date_time_obj = datetime.strptime(rain_info[0], '%d')
                x = rain_info
                rainfall_dict.update({rain_info[0]:rain_info[1]})

                # rain_info.append(tuple((line[s:e]).split()))
    return rainfall_dict




file_name = 'little_rain.txt'
print(read_file_to_list(file_name))
