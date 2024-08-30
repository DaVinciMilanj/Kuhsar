from django import forms
from .models import RentRoom
from django_jalali.forms import jDateField, jDateInput


class RentRoomForm(forms.ModelForm):
    start_date = jDateField(widget=jDateInput(attrs={'class': 'form-control'}))
    end_date = jDateField(widget=jDateInput(attrs={'class': 'form-control'}))
    best_date = jDateField(widget=jDateInput(attrs={'class': 'form-control'}))
    golden_date = jDateField(widget=jDateInput(attrs={'class': 'form-control'}))

    class Meta :
        model = RentRoom
        fields = ['user','price', 'discount', 'start_date', 'end_date', 'best_date', 'golden_date' ]
