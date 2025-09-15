from django.db import models
from django.contrib import admin

class Car(models.Model):
    carName = models.CharField(max_length=20)
    carNum = models.CharField(primary_key=True,max_length=20)
    buyerName = models.CharField(max_length=20)
    carYear = models.IntegerField()

class CarAdmin(admin.ModelAdmin):
    list_display = ['carName','carNum','buyerName','carYear']
     

