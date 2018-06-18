from django.apps import AppConfig
from django.db import models

from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=128)
    toppings = models.ManyToManyField(
        Topping,
        related_name='pizzas',
    )

    def __str__(self):
        return self.name