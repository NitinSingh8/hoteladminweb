from django.core import validators
from django import forms


class BookRoom(forms.Form):
    firstname = forms.CharField(required=True)
    lastname = forms.CharField()
    email = forms.EmailField()
    roomno = forms.IntegerField()
    starttime = forms.DateTimeField(required=False)
    endtime = forms.DateTimeField(required=False)
    roomtype = forms.CharField(widget=forms.HiddenInput, required=False)


class RoomForm(forms.Form):
    email = forms.EmailField()
