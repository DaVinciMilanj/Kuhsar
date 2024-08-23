from django.shortcuts import render
from .models import *
from django.utils import timezone
from django.views import generic


# Create your views here.
# def rent_users(request):
#     bill = RentRoom.objects.filter(user_id=request.user.id)
#     context = {'bill': bill}
#     return render(request, 'rent/userRent.html', context)
#

class RentUsersView(generic.ListView):
    model = RentRoom
    template_name = 'rent/userRent.html'
    context_object_name = 'bill'

    def get_queryset(self):
        return RentRoom.objects.filter(user_id=self.request.user.id)
