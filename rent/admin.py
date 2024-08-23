from django.contrib import admin
from .models import *


# Register your models here.

class AdminRent(admin.ModelAdmin):
    fields = ['user','price', 'discount', 'start_date', 'end_date', 'best_date', 'golden_date' ]


admin.site.register(RentRoom, AdminRent)


admin.site.register(RentHistory)