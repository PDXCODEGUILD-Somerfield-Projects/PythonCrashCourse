from django.db import models
import tzwhere

class Time_by_timezone(models.Model):
    time = models.DateTimeField()
    timezone = models.CharField(max_length = 100)
    latitude = models.FloatField()

    def __str__(self):
        return self.time

    def __repr__(self):
        return r'(%s, %r)' % (self.timezone, self.time)
