from django.shortcuts import render
from . logic import getTimeZone, getTimeInTimezone, getTimeAtTimezoneByISO8601
import datetime
import arrow

# Create your views here.

def homepage(request):
    '''
    set up initial page
    :param request:
    :return:
    '''
    return render(request, 'home.html')


def currentDateTime(request):
    '''
    gets current date time in DateTime format
    :param request:
    :return:
    '''
    now = arrow.now()
    return render(request, 'time.html', {'now': now})


def timeZone(request, latitude, longitude):
    '''
    gets timezone from latitude longitude request
    :param request:
    :param lat:
    :param long:
    :return:
    '''
    latitude = float(latitude)
    longitude = float(longitude)
    tz = getTimeZone(latitude, longitude)
    return render(request, 'time.html', {'tz': tz})

def timeInTimezone(request, latitude, longitude):
    '''
    gets time from latitude and longitude request
    :param request:
    :param latitude:
    :param longitude:
    :return:
    '''
    latitude = float(latitude)
    longitude = float(longitude)
    time = getTimeInTimezone(latitude, longitude)
    return render(request, 'time.html', {'time': time})

def TimeAtTimezoneByISO8601(request, time, latitude, longitude):
    '''
    gets time by latitude, longitude and offset query time request
    :param request:
    :param time:
    :param latitude:
    :param longitude:
    :return:
    '''
    latitude = float(latitude)
    longitude = float(longitude)
    ISO8601time = arrow.get(time)
    tz_offset_time = getTimeAtTimezoneByISO8601(ISO8601time, latitude, longitude)
    return render(request, 'time.html', {'tz_offset_time': tz_offset_time})
