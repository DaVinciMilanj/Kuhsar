from django import forms
from .models import RentRoom
from django_jalali.forms import jDateField, jDateInput
from django_jalali.admin.widgets import AdminjDateWidget





class RentRoomForm(forms.ModelForm):
    start_date = jDateField(widget=AdminjDateWidget)
    end_date = jDateField(widget=AdminjDateWidget)
    best_date = jDateField(widget=AdminjDateWidget)
    golden_date = jDateField(widget=AdminjDateWidget, required=False)
    class Meta:
        model = RentRoom
        fields = ['user', 'price', 'discount', 'start_date', 'end_date', 'best_date', 'golden_date']
