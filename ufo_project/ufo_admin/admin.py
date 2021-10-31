from django.contrib import admin
from ufo_admin.models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['CategoryName']


admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['ProductName']


admin.site.register(Product, ProductAdmin)
