from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomeUserChangeForm , CustomUserCreationForm
from .models import *
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomeUserChangeForm
    model = CustomeUser
    fieldsets = UserAdmin.fieldsets + (
        (None , {'fields': ('phone',)}),
        (None , {'fields': ('room_id' ,)}),
        (None, {'fields': ('room_size',)}),
        (None, {'fields': ('status',)})
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None , {'fields': ('phone',)}),
        (None , {'fields': ('room_id' ,)}),
        (None, {'fields': ('room_size',)}),
        (None, {'fields': ('status',)})
    )


admin.site.register(CustomeUser,CustomUserAdmin)