from django import forms
from .models import Person
from django.utils import timezone


class AddUserForm(forms.Form):
    first_name = forms.CharField(label="Your first name", max_length=50)
    last_name = forms.CharField(label="Your last name", max_length=50)
    birth_date = forms.DateField(label="Your birthdate")
    city = forms.CharField(label='Resident city', max_length=30)
    photo = forms.ImageField(required=False)
    bio = forms.CharField(max_length=100, required=False)