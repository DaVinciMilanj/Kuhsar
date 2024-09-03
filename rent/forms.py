from django import forms
from .models import RentRoom
from django_jalali import forms as jforms
from django_jalali.forms import jDateField, jDateInput
from django_jalali.admin.widgets import AdminjDateWidget



class RentRoomForm(forms.ModelForm):
    start_date = jforms.jDateField(
        widget=jforms.jDateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False
    )
    end_date = jforms.jDateField(
        widget=jforms.jDateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False
    )
    best_date = jforms.jDateField(
        widget=jforms.jDateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False
    )
    golden_date = jforms.jDateField(
        widget=jforms.jDateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = RentRoom
        fields = ['user', 'price', 'discount', 'start_date', 'end_date', 'best_date', 'golden_date']