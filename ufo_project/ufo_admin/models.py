from django.db import models


# Create your models here.

class Category(models.Model):
    CategoryId = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=100, blank=True)
    CategoryDescription = models.TextField()
    CetegoryImage = models.FileField(upload_to='category')
    CategoryCreated = models.DateField(auto_now_add=True)
    CategoryUpdated = models.DateField(auto_now=True)


class Product(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=100, blank=True)
    Category = models.CharField(max_length=100, blank=True)
    Price = models.IntegerField(blank=True)
    StrikedPrice = models.IntegerField(blank=True)
    ProductDescription = models.TextField()
    Stock = models.IntegerField(blank=True, default=1)
    ProductImage1 = models.FileField(upload_to='product_image1')
    ProductImage2 = models.FileField(upload_to='product_image2')
    ProductImage3 = models.FileField(upload_to='product_image3')
    Available = models.BooleanField(default=True)
    ProductCreated = models.DateField(auto_now_add=True)
    ProductUpdated = models.DateField(auto_now=True)
