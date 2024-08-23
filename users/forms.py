from django import forms
from rent.models import CustomeUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomeUser
        fields = UserCreationForm.Meta.fields + ('phone', 'room_id')


class CustomeUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomeUser
        fields = UserCreationForm.Meta.fields + ('phone', 'room_id')


class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    f_name = forms.CharField(max_length=50)
    l_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=15)
    room_id = forms.CharField(max_length=5)
    room_size = forms.IntegerField()
    password = forms.CharField(max_length=50)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if CustomeUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError('تلفن وارد شده تکراری است')
        return phone
