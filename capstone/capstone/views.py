from django.shortcuts import render
from django.views.decorators import cache
from django.http import JsonResponse


def landingpage(request):
    return render(request, 'capstone/base.html')

def latlong(request, lat=None, lng=None):
    my_lat = request.GET.get('lat')
    my_long = request.GET.get('lng')
    return JsonResponse({'lat': my_lat, 'lng': my_long})



# def base(request, lat=None, lng=None):
#     # latitude = request.GET.get('lat')
#     # longitude = request.GET.get('lng')
#     hit = 'some stuff'
#     return render(request, 'capstone/base.html', {'hit': hit})

