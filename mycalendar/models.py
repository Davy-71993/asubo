import datetime
from django.db import models
from django.urls import reverse
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    fro_date = models.DateField(blank=True, null=True)
    fro_time = models.TimeField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    to_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.name
