from django.db import models

class Punchlist(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    description = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    contractor = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    commitment = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    finishdate = models.DateField(null=True, blank=True)

