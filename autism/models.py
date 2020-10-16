from django.contrib import admin
from django.db import models
from datetime import date

class predict(models.Model):

    type1 = models.CharField(max_length=200, blank=False)
    type2 = models.CharField(max_length=200, blank=False)
    type3 = models.CharField(max_length=200, blank=False)
    type4 = models.CharField(max_length=200, blank=False)
    type5 = models.CharField(max_length=200, blank=False)
    type6 = models.CharField(max_length=200, blank=False)
    type7 = models.CharField(max_length=200, blank=False)
    type8 = models.CharField(max_length=200, blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} for date: {1}'.format(self.type1)
