from django.shortcuts import render
from .models import *
from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RentRoomForm
from django.urls import reverse_lazy


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


class RentRoomAdmin(LoginRequiredMixin, generic.CreateView):
    form_class = RentRoomForm
    template_name = 'rent/admin-rent.html'
    context_object_name = 'form'
    success_url = reverse_lazy('users:admin_page')





class RentRoomDetails(generic.DetailView):
    model = RentRoom
    template_name = 'rent/rent-details.html'
    context_object_name = 'bill'
