from datetime import datetime
from django.db import models

# Create your models here.


class HotelData(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    email = models.EmailField(unique=True)
    roomno = models.IntegerField()
    roomtype = models.TextField()
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    bookedtime = models.DateTimeField(blank=True, default=datetime.now())
    amountpaid = models.FloatField()


class MoneySystem(models.Model):
    money = models.FloatField()
