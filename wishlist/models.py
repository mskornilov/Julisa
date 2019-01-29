from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
# Create your models here.

class WishlistEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
