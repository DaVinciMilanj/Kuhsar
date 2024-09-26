from django import forms
from .models import *
from django_jalali.forms import jDateField, jDateInput
from django_jalali.admin.widgets import AdminjDateWidget
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from django_jalali.forms import jDateField
from .widgets import JalaliDateWidget
#

class RentRoomForm(forms.ModelForm):
    start_date = forms.CharField(widget=JalaliDateWidget())
    end_date = forms.CharField(widget=JalaliDateWidget())
    best_date = forms.CharField(widget=JalaliDateWidget())
    golden_date = forms.CharField(required=False, widget=JalaliDateWidget())

    class Meta:
        model = RentRoom
        fields = ['user', 'start_date', 'end_date', 'best_date', 'golden_date', 'price', 'discount', 'detail']

    def clean_start_date(self):
        return self.convert_jalali_to_gregorian('start_date')

    def clean_end_date(self):
        return self.convert_jalali_to_gregorian('end_date')

    def clean_best_date(self):
        return self.convert_jalali_to_gregorian('best_date')

    def clean_golden_date(self):
        golden_date = self.cleaned_data.get('golden_date')
        if golden_date:
            return self.convert_jalali_to_gregorian('golden_date')
        return None

    def convert_jalali_to_gregorian(self, field_name):
        jalali_date = self.cleaned_data.get(field_name)
        try:
            year, month, day = map(int, jalali_date.split('/'))
            gregorian_date = jdatetime.date(year, month, day).togregorian()
            return gregorian_date
        except Exception:
            raise forms.ValidationError("تاریخ وارد شده نامعتبر است.")