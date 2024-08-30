from django.contrib import admin
from .models import *


# Register your models here.

class AdminRent(admin.ModelAdmin):
    fields = ['user', 'price', 'discount', 'start_date', 'end_date', 'best_date', 'golden_date' , 'detail']
    list_display = ['user_room_id', 'price', 'start_date', 'end_date' , 'total_price']
    search_fields = ['user__room_id', 'start_date']

    def user_room_id(self, obj):
        return obj.user.room_id

    user_room_id.short_description = 'Room ID'


admin.site.register(RentRoom, AdminRent)

admin.site.register(RentHistory)
