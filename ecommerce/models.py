from django.db import models
from django.contrib.auth.models import User
from utils.model_abstracts import Model
from django_extensions.db.models import (TimeStampedModel, ActivatorModel, TitleSlugDescriptionModel)

class Item(TimeStampedModel, ActivatorModel, TitleSlugDescriptionModel, Model):

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ["id"]
    
    def __str__(self) -> str:
        return self.title
    
    stock = models.IntegerField(default=1)
    price = models.IntegerField(default=0)

    def amount(self):
        amount = float(self.price/100)
        return amount
    
    def manage_stock(self, quantity):
        self.stock -= int(quantity)
        self.save()

    def check_stock(self, quantity):
        return (int(quantity) <= self.stock)
    
    def place_order(self, user, quantity):
        if self.check_stock(quantity):
            order = Order.objects.create(item=self, quantity=quantity, user=user)
            self.manage_stock(quantity)
            return order
        else:
            return None
        

class Order(TimeStampedModel, ActivatorModel, Model):
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["id"]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE, blank=True)
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.item.title}"