from idlelib.textview import view_file

from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('admin_page' , views.AdminPage.as_view(), name='admin_page'),
    path('user_page' , views.user_page, name='user_page'),
    path('logout' , views.LogoutUser.as_view() , name='logout_user'),
    path('register/' , views.RegisterUserPage.as_view(), name='register'),
    path('datails/<int:id>' , views.admin_details , name='admin_details')
]
