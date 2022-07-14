from django.db import models
from staff.models import StaffUser


PAYMENT_CHOICES = (
    ('card','CARD'),
    ('cash', 'CASH'),
    ('upi','UPI'),
    ('coupons','CPOUPONS'),
)


class FoodCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    description = models.TextField()
    available = models.BooleanField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_veg = models.BooleanField()
    quantity = models.IntegerField()
    reciepe = models.JSONField()

    def __str__(self):
        return self.name


class Ingridients(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    available = models.BooleanField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Orders(models.Model):
    customer_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length = 10)
    table_num = models.IntegerField()
    total = models.IntegerField()
    payment_method = models.CharField(max_length=7, choices=PAYMENT_CHOICES, default='card')
    delievery_boy = models.ForeignKey(StaffUser, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=True)
    is_cancelled_by_user = models.BooleanField(default=False)
    prep_time = models.CharField(default="30m", max_length=3)

    def __str__(self):
        return self.customer_name


    