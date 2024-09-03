from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomeUser(AbstractUser):
    STATUS = (
        ('admin' , 'admin') ,
        ('owner' , 'owner'),
        ('customer' , 'customer')
    )
    phone = models.CharField(max_length=13,unique=True)
    room_id = models.CharField(max_length=5 , unique=True , blank=True , null=True)
    room_size = models.PositiveIntegerField(blank=True , null=True)
    status = models.CharField(choices=STATUS , blank=True , null= True , max_length=18)

    def __str__(self):
        return str(self.room_id)
