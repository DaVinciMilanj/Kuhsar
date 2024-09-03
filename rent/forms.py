from django import forms
from .models import RentRoom
from django_jalali.forms import jDateField, jDateInput




class RentRoomForm(forms.ModelForm):
    # start_date = jDateField(widget=jDateInput() )
    # end_date = jDateField(widget=jDateInput())
    # best_date = jDateField(widget=jDateInput())
    # golden_date = jDateField(widget=jDateInput())

    class Meta:
        model = RentRoom
        fields = ['user', 'price', 'discount', 'start_date', 'end_date', 'best_date', 'golden_date']



