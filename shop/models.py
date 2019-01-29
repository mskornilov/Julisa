from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField('Название', max_length=250)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
