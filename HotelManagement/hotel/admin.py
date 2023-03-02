from django.contrib import admin
from .models import HotelData, MoneySystem
# Register your models here.


@admin.register(HotelData)
class AdminHotelData(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'roomno',
                    'roomtype', 'starttime', 'endtime', 'bookedtime', 'amountpaid')


@admin.register(MoneySystem)
class AdminMoneySystem(admin.ModelAdmin):
    list_display = ('id', 'money',)
