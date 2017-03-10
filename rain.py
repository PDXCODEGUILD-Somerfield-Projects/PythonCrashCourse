"""Reads history of rainfall at Sunnyside school and determines rain records"""
import re
from datetime import datetime

month_dict = {'JAN' : 1, 'FEB' : 2, 'MAR' : 3, 'APR' : 4, 'MAY' : 5, 'JUN' : 6, 'JUL' : 7, 'AUG' : 8, 'SEP' : 9,
           'OCT' : 10, 'NOV' : 11, 'DEC' : 12}

def read_file_to_list(file_name):
    """Opens rain-data file and creates a list of dates with corresponding rainfall
<<<<<<< HEAD
=======

>>>>>>> connect-four-one
    :param file_name:
    :return: dictionary {date : rainfall}
    """
    rainfall_dict = {}
    with open(file_name) as rain_file:
        for line in rain_file.readlines():
            # searches for the date and total in the line
            info_match = re.search('\d\d[-]\w{3}[-]\d{4}\s*\d*', line)
            if info_match != None:
                s = info_match.start()
                e = info_match.end()
                rain_info = (line[s:e].split())
                date_string = convert_date_to_std_format(rain_info[0])
                # add reformatted date back into the string
                rain_info[0] = date_string
                if len(rain_info) > 1:
                    # changes the number to the .01 format to better reflect the data
                    rain_info[1] = float(rain_info[1]) * .01
                    # adds the date and total to the dictionary
                    rainfall_dict.update({rain_info[0]:rain_info[1]})
    return rainfall_dict

def convert_date_to_std_format(date_string):
    """Takes date from text file and changes it to YYYY-M-DD format
<<<<<<< HEAD
=======

>>>>>>> connect-four-one
    :param date_string:
    :return: date string in YYYY-M-DD format
    """
    # finds month in the string
    month_match = re.search('\w{3}', date_string)
    if month_match != None:
        m_s = month_match.start()
        m_e = month_match.end()
        month_str = date_string[m_s:m_e]
    # assigns corresponding number to month (ex> MAR : 3)
    month_num = str(month_dict.get((date_string)[m_s:m_e]))
    # parses out year, day
    year = date_string[-4:]
    day = date_string[:2]
    # concatenates the new date string
    std_date_string = year + '-' + month_num + '-' + day
    return std_date_string

def day_with_most_rain(rainfall_dict):
    """Determines the day with most rain and returns list of (day, amount)
<<<<<<< HEAD
=======

>>>>>>> connect-four-one
    :param rainfall_dict:
    :return: list of amount of max rain and date(s)
    >>> day_with_most_rain({'2016-3-30': 0, '2016-3-29': 0, '2016-3-28': 2, '2016-3-27': 5, '2016-3-26': 5, '2016-3-25': 0, '2016-3-24': 6})
    ['6', '2016-3-24']
<<<<<<< HEAD
    >>> day_with_most_rain({'2016-3-30': 0, '2016-3-29': 10, '2016-3-28': 2, '2016-3-27': 5, '2016-3-26': 10, '2016-3-25': 0, '2016-3-24': 6})
    ['10', '2016-3-29', '2016-3-26']
=======

    >>> day_with_most_rain({'2016-3-30': 0, '2016-3-29': 10, '2016-3-28': 2, '2016-3-27': 5, '2016-3-26': 10, '2016-3-25': 0, '2016-3-24': 6})
    ['10', '2016-3-29', '2016-3-26']

>>>>>>> connect-four-one
    """
    # finds the highest total inches for one day
    rainfall_inches = []
    for inches in rainfall_dict.values():
        rainfall_inches.append(inches)
    max_value = max(rainfall_inches)

    # creates a list of dates that match that max total
    heaviest_rainfall_dates = []
    for date, inches in rainfall_dict.items():
        if inches == max_value:
            heaviest_rainfall_dates.append(date)
    # creates a list of max-rainfall, dates
    max_value = [str(max_value)]
    max_rain_with_dates = max_value + heaviest_rainfall_dates

    return max_rain_with_dates

def list_years_by_rainfall(rainfall_dict):
    """Creates a list of lists of years and their total rainfall
<<<<<<< HEAD
=======

>>>>>>> connect-four-one
    :param rainfall_dict:
    :return:
    >>> list_years_by_rainfall({'2014-3-30': 0, '2012-3-29': 10, '2015-3-28': 2, '2016-3-27': 5, '2011-3-26': 7, '2012-3-25': 7, '2007-3-24': 6})
    [['2007', 6], ['2011', 7], ['2012', 17], ['2014', 0], ['2015', 2], ['2016', 5]]
    """
    rain_by_year_list = []
    for date, inches in rainfall_dict.items():
        year = date[:4]
        if len(rain_by_year_list) < 1:
            rain_by_year_list.append([year, inches])
        else:
            for index, list in enumerate(rain_by_year_list):
                in_list = False
                if year in list[0]:
                    rain_by_year_list[index][1] += inches
                    in_list = True
                    break
            if in_list == False:
                rain_by_year_list.append([year, inches])
    rain_by_year_list.sort()
    return rain_by_year_list

def year_with_most_rain(rain_by_year_list):
    """Determines the year on record with the most rainfall
<<<<<<< HEAD
=======

>>>>>>> connect-four-one
    :param rainfall_dict:
    :return: list with max amount of rainfall, year(s) with that max amount
    >>> year_with_most_rain([['2007', 6], ['2011', 7], ['2012', 17], ['2014', 0], ['2015', 2], ['2016', 5]])
    [17, '2012']
    """
    max_rainfall = 0
    years_with_max = []
    for index, list in enumerate(rain_by_year_list):
        if list[1] > max_rainfall:
            max_rainfall = list[1]
    for list in rain_by_year_list:
        if list[1] == max_rainfall:
            years_with_max.append(list[0])
    max_rain_and_year = [max_rainfall, years_with_max]
    return max_rain_and_year

def average_by_day_dict(rainfall_dict):
    for date, amount in rainfall_dict.items():
        date[4:]


def main():
    # reads the rain stats file and creates a dictionary of rainfall by date
    file_name = 'rain.txt'
    rainfall_dict = read_file_to_list(file_name)

    # finds the date with the most rain
    max_rain_with_dates = day_with_most_rain(rainfall_dict)
    # formats the gathered date to a read-friendly format
    format_max_rain_date = datetime.strptime(max_rain_with_dates[1], '%Y-%m-%d').strftime('%-m/%d/%y')

    # finds the year with the most rain
    list_of_years_and_rainfall = list_years_by_rainfall(rainfall_dict)
    max_rainfall_yr = year_with_most_rain(list_of_years_and_rainfall)

    # prints the results:
    if len(max_rain_with_dates) == 2:
        print('The day with the most rainfall on record is ' + format_max_rain_date +
              ' with ' + max_rain_with_dates[0] + ' inches of rain.')
    else:
        print('The days with the most rainfall on record are ', end='')
        for index in max_rain_with_dates[1:]:
            print(index + ', ', end='')
        print(' with ' + format_max_rain_date + ' inches of rain')

    print('The year with the most rainfall is ' + ''.join(max_rainfall_yr[1]) + ' with ' +
          str('{0:.2f}'.format(round(max_rainfall_yr[0], 2))) + ' inches.')



if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> connect-four-one
