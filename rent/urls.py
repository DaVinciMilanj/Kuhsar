from django.urls import path
from . import views
from django.conf.urls.static import static
app_name = 'rent'
urlpatterns = [
    path('' , views.RentUsersView.as_view() , name='rent_users'),
    path('admin-rent' , views.RentRoomAdmin.as_view() , name='admin_rent'),
    path('admin-rent-details/<int:pk>' , views.AdminRentRoomDetails.as_view() , name='admin_rent_details'),
    path('rent-details/<int:pk>' , views.RentRoomDetails.as_view() , name='rent_details'),
    path('all-rent/<int:pk>' , views.AllRentUser.as_view() , name='all_rent')
]
 