from django.shortcuts import render
from django.http import JsonResponse
from .oauth import get_twitter_token


def landingpage(request):
    user_token = get_twitter_token()
    return render(request, 'capstone/landing.html')

def base(request):
    return render(request, 'capstone/base.html')

def latlong(request, lat=None, lng=None):
    my_lat = request.GET.get('lat')
    my_long = request.GET.get('lng')
    lat_long_json = JsonResponse({'lat': my_lat, 'lng': my_long})
    return lat_long_json





