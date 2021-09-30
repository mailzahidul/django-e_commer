from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Product(models.Model):
    title = models.CharField(max_length = 100)
    price = models.FloatField()
    discount_price =  models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media/product/')

    def __str__(self):
        return self.title
