from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .models import CustomeUser


# Create your views here.

# def home(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             try:
#                 user = authenticate(request, username=CustomeUser.objects.get(phone=data['user']),
#                                     password=data['password'])
#             except:
#
#                 user = authenticate(request, username=data['user'], password=data['password'])
#
#             if user is not None:
#                 login(request, user)
#                 if user.is_staff:
#                     return redirect('users:admin_page')
#                 else:
#                     return redirect('users:user_page')
#
#     else:
#         form = LoginForm()
#
#     return render(request, 'users/login.html', {'form': form})
#

class HomePageView(generic.FormView):
    template_name = 'users/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        try:
            user = authenticate(request, username=CustomeUser.objects.get(phone=data['user']),
                                password=data['password'])
        except:
            user = authenticate(request, username=data['user'], password=data['password'])
        if user is not None:
            login(self.request, user)
            if user.is_staff:
                return redirect('users:admin_page')
            else:
                return redirect('users:user_page')
        else:
            return self.form_invalid(form)


def admin_page(request):
    return render(request, 'users/admin.html')


def user_page(request):
    return render(request, 'users/users.html')


# def register_user(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = CustomeUser.objects.create(username=data['username'], first_name=data['f_name'],
#                                               last_name=data['l_name'], phone=data['phone']
#                                               , room_id=data['room_id'], room_size=data['room_size'],
#                                               password=['password'], status='owner')
#             user.save()
#             return redirect('users:register')
#     else:
#         form = RegisterForm()
#
#     return render(request, 'users/register.html', {'form': form})


class RegisterUserPage(generic.FormView):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        data = form.cleaned_data
        user = CustomeUser.objects.create(username=data['username'], first_name=data['f_name'],
                                          last_name=data['l_name'], phone=data['phone']
                                          , room_id=data['room_id'], room_size=data['room_size'],
                                          status='owner')
        user.set_password(data['password'])
        user.save()
        return redirect('users:register')


# def logout_user(request):
#     logout(request)
#     return redirect('users:home')


class LogoutUser(LogoutView):
    next_page = 'users:home'
