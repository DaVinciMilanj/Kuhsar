from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django_jalali.db import models as jmodels
from users.models import CustomeUser
from django.db.models.signals import post_save


# Create your models here.

class RentRoom(models.Model):
    user = models.ForeignKey(CustomeUser, limit_choices_to={'status': 'owner'}, on_delete=models.CASCADE,
                             related_name='user_rent')
    price = models.PositiveIntegerField()
    start_date = jmodels.jDateField()
    end_date = jmodels.jDateField()
    best_date = jmodels.jDateField()
    golden_date = jmodels.jDateField(blank=True)
    discount = models.PositiveSmallIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    total_price = models.PositiveIntegerField(blank=True, null=True)
    paid = models.BooleanField(default=False)
    create = jmodels.jDateTimeField(auto_now_add=True)
    update = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.user.room_id

    @property
    def total_price(self):
        time = timezone.now().date()

        if self.discount:
            if self.start_date <= time <= self.golden_date:
                total = int(self.price * self.user.room_size)
                offer = (total * self.discount) / 100
                return int(total - offer)
            elif time > self.golden_date:
                total = self.price * self.user.room_size
                return int(total)


        elif not self.discount:
            total = self.price * self.user.room_size
            return int(total)


class RentHistory(models.Model):
    user = models.ForeignKey(CustomeUser, on_delete=models.CASCADE, related_name='user_history')
    price = models.PositiveIntegerField(blank=True)
    paid = models.BooleanField(default=False)
    # total_price = models.PositiveBigIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    paid_change = models.DateTimeField(auto_now=True)


def rent_history_save(sender, instance, created, *args, **kwargs):
    data = instance
    if created:
        RentHistory.objects.create(user=data.user, price=data.price, created=data.create, paid_change=data.update,
                                   )


post_save.connect(rent_history_save, sender=RentRoom)
