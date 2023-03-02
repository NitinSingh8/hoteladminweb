import datetime
import math
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import BookRoom, RoomForm
from django.contrib import messages
from .models import HotelData, MoneySystem

# Create your views here.

amount_per_room_type = {'A': 100, 'B': 80, 'C': 50}
overlap = {'A': 2, 'B': 3, 'C': 5}


def home(request):
    if request.method == "POST":
        fm = BookRoom(request.POST)
        if fm.is_valid():
            fn = fm.cleaned_data["firstname"]
            ln = fm.cleaned_data["lastname"]
            em = fm.cleaned_data["email"]
            rn = fm.cleaned_data["roomno"]
            st = fm.cleaned_data["starttime"]
            et = fm.cleaned_data["endtime"]
            rt = fm.cleaned_data["roomtype"]

            hotelobj = HotelData.objects.filter(roomtype=rt)
            print(hotelobj)
            hotelobj = hotelobj.filter(roomno=rn)

            print("hotel obj : ", hotelobj)
            li = []
            for query in hotelobj:
                li.append([query.starttime, query.endtime])

            if (st > et):
                print("Not possible")
                messages.warning(
                    request, "Start time must be smaller than End time")
                fm = BookRoom()
                return render(request, 'hotel/index.html', {'form': fm})

            overlapping = 0

            for a, b in li:
                if a < st and b < st:
                    continue
                if a > et and b > et:
                    continue
                else:
                    overlapping += 1

            if overlapping >= 1:
                messages.warning(
                    request, "This slot is not available for booking")
                fm = BookRoom()
                return render(request, 'hotel/index.html', {'form': fm})

            # print(fm.cleaned_data)
            print(fn, ln, em, rn, rt, st, et)
            dt = et - st
            print(dt)
            no_hours = math.ceil(dt.seconds/60/60)
            no_hours += (dt.days*24)
            print(no_hours)

            try:

                amt = no_hours*amount_per_room_type[rt]
                obj = HotelData(firstname=fn, lastname=ln, email=em,
                                roomno=rn, roomtype=rt, starttime=st, endtime=et, amountpaid=amt)
                obj.save()

                rows = MoneySystem.objects.all()
                print(rows)
                if rows:
                    amt = MoneySystem.objects.get(pk=1)
                    amount = amt.money
                    amount += no_hours*amount_per_room_type[rt]
                    print(amount)
                    user = MoneySystem(pk=1, money=amount)
                    user.save()
                else:
                    user = MoneySystem(pk=1, money=amt)
                    user.save()
                messages.success(request, "Room Booked Successfully")
                return HttpResponseRedirect('/view/1')
            except Exception as e:
                print(e)
                messages.warning(request,
                                 "Email should be unique and filled all the data")
                fm = BookRoom()
                return render(request, 'hotel/index.html', {'form': fm})

        else:
            print("invalid")
            fm = BookRoom()
            return render(request, 'hotel/index.html', {'form': fm})
    else:
        fm = BookRoom()
        return render(request, 'hotel/index.html', {'form': fm})


def history(request, my_id):

    totalqueries = MoneySystem.objects.all()
    if len(totalqueries) == 0:
        mn = 0
    else:
        moneyobj = MoneySystem.objects.get(pk=1)
        mn = moneyobj.money
    roomno_filter = None
    roomtype_filter = None
    starttime_filter = None
    if my_id == 1:
        data = HotelData.objects.all().order_by('roomno', 'roomtype')
        val = "Room No."
        roomno_filter = True
    elif my_id == 2:
        data = HotelData.objects.all().order_by('roomtype')
        val = "Room Type"
        roomtype_filter = True
    elif my_id == 3:
        data = HotelData.objects.all().order_by('starttime')
        val = "Start Time"
        starttime_filter = True

    else:
        data = HotelData.objects.all()
        val = "Default"
    return render(request, 'hotel/view_data.html', {'data': data, 'filter': val, 'money': mn, 'roomno_filter': roomno_filter, 'roomtype_filter': roomtype_filter, 'starttime_filter': starttime_filter})


def update(request):
    if (request.method == "POST"):
        fm = RoomForm(request.POST)
        if fm.is_valid():
            em = fm.cleaned_data['email']
            if HotelData.objects.filter(email=em).exists():
                data = HotelData.objects.get(email=em)
                print(data.starttime)
                print(data.endtime)
                start = str(data.starttime)[:10]+"T"+str(data.starttime)[11:16]
                end = str(data.endtime)[:10]+"T"+str(data.endtime)[11:16]
                userfm = BookRoom()
                return render(request, 'hotel/update_data.html', {"data": data, "st": start, "et": end, "form": fm, "email": em, "user_form": userfm})
            else:
                messages.warning(
                    request, "Room with this email not Booked Yet")
                fm = RoomForm()
                return render(request, 'hotel/update_data.html', {'data': None, 'form': fm})
        else:
            print("INVALID FORM")
            messages.warning(
                request, "Soemthing wrong in input, Kindly fill it again")
            fm = RoomForm()
            return render(request, 'hotel/update_data.html', {'data': None, 'form': fm})

    else:
        fm = RoomForm()
        # if my_id == 0:
        return render(request, 'hotel/update_data.html', {"data": None, "form": fm})


def update_data(request, my_id):
    if request.method == 'POST':
        fm = BookRoom(request.POST)
        if fm.is_valid():
            fn = fm.cleaned_data["firstname"]
            ln = fm.cleaned_data["lastname"]
            em = fm.cleaned_data["email"]
            rn = fm.cleaned_data["roomno"]
            st = fm.cleaned_data["starttime"]
            et = fm.cleaned_data["endtime"]
            rt = fm.cleaned_data["roomtype"]

            hotelobj = HotelData.objects.filter(roomtype=rt)
            hotelobj = hotelobj.filter(roomno=rn)
            li = []
            for query in hotelobj:
                li.append([query.starttime, query.endtime])

            if (st > et):
                print("Not possible")
                messages.warning(
                    request, "Start time must be smaller than End time")
                fm = BookRoom()
                return render(request, 'hotel/update_data.html', {'form': fm})
            overlapping = 0
            print(li)

            for a, b in li:

                if a < st and b < st:
                    continue
                if a > et and b > et:
                    continue
                else:
                    overlapping += 1
            print(overlapping)
            if overlapping > 1:
                messages.warning(
                    request, "This slot is not available for booking")
                fm = BookRoom()
                return render(request, 'hotel/update_data.html', {'form': fm})

            # print(fn, ln, em, rn, rt, st, et)
            prevobj = HotelData.objects.get(id=my_id)
            prevrt = prevobj.roomtype
            dt = et - st
            # print(dt)
            no_hours = math.ceil(dt.seconds/60/60)
            no_hours += (dt.days*24)
            # print(prevrt)

            try:
                amt = no_hours*amount_per_room_type[rt]
                obj = HotelData(id=my_id, firstname=fn, lastname=ln, email=em,
                                roomno=rn, roomtype=rt, starttime=st, endtime=et, amountpaid=amt)
                obj.save()
                moneyobj = MoneySystem.objects.get(pk=1)
                mn = moneyobj.money
                mn -= prevobj.amountpaid
                mn += amt
                currmoneyobj = MoneySystem(pk=1, money=mn)
                currmoneyobj.save()

                messages.success(request, "Room Update Successfully")
                return HttpResponseRedirect('/update')
            except Exception as e:

                messages.warning(request,
                                 "Email Should be Unque. Delete your previous booking first ")
                fm = BookRoom()
                return render(request, 'hotel/update_data.html', {'data': None, 'form': fm})

        else:
            print("invalid")
    return HttpResponseRedirect('/update/')


def delete(request):
    if request.method == "POST":
        fm = RoomForm(request.POST)
        if fm.is_valid():
            em = fm.cleaned_data['email']
            if HotelData.objects.filter(email=em).exists():
                data = HotelData.objects.get(email=em)
                start = str(data.starttime)[:10]+"T"+str(data.starttime)[11:16]
                end = str(data.endtime)[:10]+"T"+str(data.endtime)[11:16]
                starttime = data.starttime.timestamp()
                now = datetime.datetime.today().timestamp()
                if (starttime < now):
                    ref_amt = 0
                else:
                    diff = math.ceil((starttime-now)/60/60)
                    print(starttime, now, diff)
                    if diff > 48:
                        ref_amt = data.amountpaid
                    elif diff > 24:
                        ref_amt = data.amountpaid//2
                    else:
                        ref_amt = 0
                return render(request, 'hotel/delete_data.html', {'form': fm, 'data': data, 'st': start, 'et': end, 'refund_amount': ref_amt})

            else:
                messages.warning(
                    request, "Room with this email is not Booked Yet")
                fm = RoomForm()
                return render(request, 'hotel/delete_data.html', {'form': fm, 'data': None})
    else:
        fm = RoomForm()
        return render(request, 'hotel/delete_data.html', {'form': fm, 'data': None})


def delete_data(request, my_id):
    if request.method == 'POST':
        user = HotelData(pk=my_id)
        obj = HotelData.objects.get(pk=my_id)
        starttime = obj.starttime.timestamp()
        now = datetime.datetime.today().timestamp()
        if (starttime < now):
            ref_amt = 0
        else:
            diff = math.ceil((starttime-now)/60/60)
            print(starttime, now, diff)
            if diff > 48:
                ref_amt = obj.amountpaid
            elif diff > 24:
                ref_amt = obj.amountpaid//2
            else:
                ref_amt = 0

        moneyuser = MoneySystem.objects.get(pk=1)
        mn = moneyuser.money
        mn -= ref_amt
        currmoneyuser = MoneySystem(pk=1, money=mn)
        currmoneyuser.save()

        user.delete()
        fm = RoomForm()
        messages.success(request, "Booked Room deleted")
        return HttpResponseRedirect('/view/1')
    else:
        fm = RoomForm()
        return render(request, 'hotel/delete_data.html', {'form': fm, 'data': None})


def about(request):
    return render(request, 'hotel/about.html')
