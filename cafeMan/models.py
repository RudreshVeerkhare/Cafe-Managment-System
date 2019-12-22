from django.db import models
from django.contrib.auth.models import User
import random
from django.utils import timezone

# Create your models here

class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    etp = models.PositiveIntegerField(default=0)
    special_day = models.CharField(max_length=4)
    quantity = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(default=round(random.uniform(3, 5), 1), max_digits=2, decimal_places=1)

    def __str__(self):
        return str(tuple([self.name, self.price, self.special_day]))

class Orders(models.Model):
    placed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(Dish)
    etp = models.PositiveIntegerField(default=0)
    time_placed = models.DateTimeField(default=timezone.localtime().now)
    order_active = models.BooleanField(default=True)
    otp = models.CharField(max_length=100)

    def __str__(self):
        return str(tuple([self.placed_by, self.order_items.all(), self.etp, self.order_active, self.otp]))

    def calculate_eta(self):
        if self.etp == 0:
            for dish in self.order_items.all():
                self.etp += dish.etp