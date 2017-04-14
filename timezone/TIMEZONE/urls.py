"""TIMEZONE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from TIMEZONE.views import homepage, currentDateTime, timeZone, timeInTimezone, TimeAtTimezoneByISO8601

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', homepage, name='home'),
    url(r'^time/$', currentDateTime, name='time'),
    url(r'^(?P<latitude>^([-+]?\d{1,2}([.]\d+)?)),\s*(?P<longitude>([-+]?\d{1,3}([.]\d+)?))/tz$',
        timeZone, name='timezone'),
    url(r'^(?P<latitude>^([-+]?\d{1,2}([.]\d+)?)),\s*(?P<longitude>([-+]?\d{1,3}([.]\d+)?))/time$',
        timeInTimezone, name='timezonetime'),
    url(r'^(?P<time>\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d-\d\d:\d\d)' +
        '/at/(?P<latitude>([-+]?\d{1,2}([.]\d+)?)),\s*(?P<longitude>([-+]?\d{1,3}([.]\d+)?)$)',
    TimeAtTimezoneByISO8601, name='tzISO8601')
]
# ([1-8]?\d(\.\d+)?|90(\.0+)?)),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)/tz