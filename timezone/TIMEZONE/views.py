from django.shortcuts import render
from django.http import Http404
from . logic import get_time_zone, get_time_in_timezone, get_time_at_timezone_by_ISO8601, check_lat_long_valid
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


def current_date_time(request):
    '''
    gets current date time in DateTime format
    :param request:
    :return:
    '''
    now = arrow.now()
    return render(request, 'time.html', {'now': now})


def time_zone(request, latitude, longitude):
    '''
    gets timezone from latitude longitude request
    :param request:
    :param lat:
    :param long:
    :return:
    '''
    try:
        error_msg = check_lat_long_valid(latitude, longitude)
    except error_msg != '':
        raise Http404(error_msg)
    if error_msg == '':
        tz = get_time_zone(latitude, longitude)
        return render(request, 'time.html', {'tz': tz})
    else:
        return render(request, '404.html', {'error_message': error_msg})

def time_in_timezone(request, latitude, longitude):
    '''
    gets time from latitude and longitude request
    :param request:
    :param latitude:
    :param longitude:
    :return:
    '''
    try:
        error_msg = check_lat_long_valid(latitude, longitude)
    except error_msg != '':
        raise Http404(error_msg)
    if error_msg == '':
        time = get_time_in_timezone(latitude, longitude)
        return render(request, 'time.html', {'time': time})
    else:
        return render(request, '404.html', {'error_message': error_msg})

def time_at_timezone_by_ISO8601(request, time, latitude, longitude):
    '''
    gets time by latitude, longitude and offset query time request
    :param request:
    :param time:
    :param latitude:
    :param longitude:
    :return:
    '''
    try:
        error_msg = check_lat_long_valid(latitude, longitude)
    except error_msg != '':
        raise Http404(error_msg)
    if error_msg == '':
        tz_offset_time = get_time_at_timezone_by_ISO8601(time, latitude, longitude)
        return render(request, 'time.html', {'tz_offset_time': tz_offset_time})
    else:
        return render(request, '404.html', {'error_message': error_msg})

def error400(request):
    '''
    throws a bad request message to user
    :return:
    '''
    error_msg = 'Something was wrong with the request. Please check that input was valid and try again.'
    return render(request, '400.html', {'error_message': error_msg})

def error404(request):
    '''
    throws an error message to user
    :param request:
    :return:
    '''
    error_msg = 'Something was wrong with the request. Please check that input was valid and try again.'
    return render(request, '404.html', {'error_message': error_msg})
