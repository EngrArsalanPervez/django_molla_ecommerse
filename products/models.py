from django.contrib.auth.models import User
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image1 = models.ImageField(upload_to='products_images', blank=True, null=True)
    image2 = models.ImageField(upload_to='products_images', blank=True, null=True)
    category = models.ForeignKey(Categories, related_name='products', on_delete=models.CASCADE)
    published_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    published_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
