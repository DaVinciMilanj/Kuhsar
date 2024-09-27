
from django import forms
import jdatetime

class JalaliDateWidget(forms.DateInput):
    input_type = 'text'

    def format_value(self, value):
        if value:

            return jdatetime.date.fromgregorian(date=value).strftime('%Y/%m/%d')
        return super().format_value(value)