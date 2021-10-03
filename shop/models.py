from django.db import models
from PIL import Image

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Product(models.Model):
    title = models.CharField(max_length = 100)
    price = models.FloatField()
    discount_price =  models.FloatField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product/')

    def save(self):
        super().save()                              # saving image first
        img = Image.open(self.image.path)           # Open image using self
        print(self.image.path, "path.........")
        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)               # saving image at the same path

    def __str__(self):
        return self.title



