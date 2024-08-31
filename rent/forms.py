from django import forms
from .models import RentRoom
from django_jalali.forms import jDateField, jDateInput
from django_jalali import forms as jalili_form



class RentRoomForm(forms.ModelForm):
    class Meta:
        model = RentRoom
        fields = ['user', 'price', 'discount', 'start_date', 'end_date', 'best_date', 'golden_date']
