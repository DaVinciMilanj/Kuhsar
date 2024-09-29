from django.http import HttpResponseForbidden
from django.shortcuts import render
from .models import *
from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RentRoomForm
from django.urls import reverse_lazy
from jdatetime import date, datetime
import jdatetime
from django.contrib.auth.mixins import UserPassesTestMixin


def jalali_to_gregorian(jalali_date):
    jalali_datetime = datetime.strptime(jalali_date, "%Y/%m/%d").date()
    gregorian_datetime = jalali_datetime.togregorian()
    return gregorian_datetime


# Create your views here.
# def rent_users(request):
#     bill = RentRoom.objects.filter(user_id=request.user.id)
#     context = {'bill': bill}
#     return render(request, 'rent/userRent.html', context)
#

class RentUsersView(LoginRequiredMixin, generic.ListView):
    model = RentRoom
    template_name = 'rent/userRent.html'
    context_object_name = 'bill'

    def get_queryset(self):
        return RentRoom.objects.filter(user_id=self.request.user.id)


class RentRoomAdmin(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    form_class = RentRoomForm
    template_name = 'rent/admin-rent.html'
    context_object_name = 'form'
    success_url = reverse_lazy('users:admin_page')

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.status == 'admin' or user.is_superuser)

    def handle_no_permission(self):
        return HttpResponseForbidden("شما اجازه دسترسی به این صفحه را ندارید.")

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        # در اینجا نیازی به تبدیل تاریخ نیست زیرا در فرم انجام شده است
        # اگر نیاز به پردازش اضافی دارید، می‌توانید آن را اینجا اضافه کنید
        return super().form_valid(form)


# def creat_rent(request):
#     if request.method == "POST":
#         form = RentRoomForm(request.POST)
#         if form.is_valid() :
#             data = form.cleaned_data
#             RentRoom.objects.create(user_id=data['user'] , price=data['price'] , start_date=data['start_date'] , discount=data['discount'],
#                                     end_date=data['end_date'] , best_date=data['best_date'] , golden_date=data['golden_date'])
#
#
#     else:
#         form =RentRoomForm()
#     return render(request , 'rent/admin-rent.html')

class AdminRentRoomDetails(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):
    model = RentRoom
    template_name = 'rent/admin-rent-details.html'
    context_object_name = 'bill'

    def test_func(self):
        user = self.request.user

        return user.is_authenticated and (user.status == 'admin' or user.is_superuser or user.id == self.kwargs['pk'])

    def handle_no_permission(self):
        return HttpResponseForbidden("شما اجازه دسترسی به این صفحه را ندارید.")


class RentRoomDetails(LoginRequiredMixin, generic.DetailView):
    model = RentRoom
    template_name = 'rent/rent-details.html'
    context_object_name = 'bill'


class AllRentUser(UserPassesTestMixin, generic.ListView):
    model = RentRoom
    template_name = 'rent/all-rent.html'
    context_object_name = 'bill'

    def get_queryset(self):
        rents = RentRoom.objects.filter(user_id=self.kwargs['pk'])
        return rents

    def test_func(self):
        user = self.request.user

        return user.is_authenticated and (user.status == 'admin' or user.is_superuser or user.id == self.kwargs['pk'])

    def handle_no_permission(self):
        return HttpResponseForbidden("شما اجازه دسترسی به این صفحه را ندارید.")
