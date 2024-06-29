from django.db import models

class mppr(models.Model):
    areaName = models.CharField(max_length=50)
    areaSqm = models.FloatField(max_length=50)
    work = models.CharField(max_length=50)
    manpower = models.CharField(max_length=25)
    quantity = models.SmallIntegerField()
    startdate = models.DateField(null=True, blank=True)
    finishdate =models.DateField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    rateHourPerSqm =models.FloatField(null=True, blank=True)