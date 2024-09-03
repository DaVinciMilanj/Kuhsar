from django.contrib import admin
from django import forms
from .models import RentRoom, RentHistory
from users.models import CustomeUser


class AdminRent(admin.ModelAdmin):
    fields = ['user' ,'price' ,'start_date' ,'end_date' ,'best_date' ,'detail' ,'golden_date' ,'discount']
    list_display = ['user', 'price', 'start_date', 'end_date', 'total_price' , ]
    search_fields = ['user__room_id', 'start_date']
    # readonly_fields = ['user_room_id']
    #
    # def user_room_id(self, obj):
    #     return obj.user.room_id
    #
    # user_room_id.short_description = 'Room ID'


admin.site.register(RentRoom, AdminRent)
admin.site.register(RentHistory)
