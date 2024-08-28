from django import forms
from .models import RentRoom


class RentRoomForm(forms.ModelForm):
    class Meta :
        model = RentRoom
        fields = ['user','price', 'discount', 'start_date', 'end_date', 'best_date', 'golden_date' ]
