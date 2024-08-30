from django.urls import path
from . import views
from django.conf.urls.static import static
app_name = 'rent'
urlpatterns = [
    path('' , views.RentUsersView.as_view() , name='rent_users'),
    path('admin-rent' , views.RentRoomAdmin.as_view() , name='admin_rent'),
    path('rent-details/<int:pk>' , views.RentRoomDetails.as_view() , name='rent_details')
]
 