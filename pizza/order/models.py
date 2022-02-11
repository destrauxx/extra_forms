from django.db import models
from pizza.models import PizzaModel
# Create your models here.

class OrderModel(models.Model):
    adress = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    pizza_order = models.ManyToManyField(PizzaModel)