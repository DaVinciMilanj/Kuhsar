from idlelib.textview import view_file

from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('admin_page' , views.admin_page, name='admin_page'),
    path('user_page' , views.user_page, name='user_page'),
    path('logout' , views.LogoutUser.as_view() , name='logout_user'),
    path('register' , views.RegisterUserPage.as_view(), name='register')
]
