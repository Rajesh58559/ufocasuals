# Generated by Django 3.2.7 on 2021-10-31 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CategoryId', models.AutoField(primary_key=True, serialize=False)),
                ('CategoryName', models.CharField(blank=True, max_length=100)),
                ('CategoryDescription', models.TextField()),
                ('CetegoryImage', models.FileField(upload_to='category')),
                ('CategoryCreated', models.DateField(auto_now_add=True)),
                ('CategoryUpdated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ProductId', models.AutoField(primary_key=True, serialize=False)),
                ('ProductName', models.CharField(blank=True, max_length=100)),
                ('Category', models.CharField(blank=True, max_length=100)),
                ('Price', models.IntegerField(blank=True)),
                ('StrikedPrice', models.IntegerField(blank=True)),
                ('ProductDescription', models.TextField()),
                ('Stock', models.IntegerField(blank=True, default=1)),
                ('ProductImage1', models.FileField(upload_to='product_image1')),
                ('ProductImage2', models.FileField(upload_to='product_image2')),
                ('ProductImage3', models.FileField(upload_to='product_image3')),
                ('Available', models.BooleanField(default=True)),
                ('ProductCreated', models.DateField(auto_now_add=True)),
                ('ProductUpdated', models.DateField(auto_now=True)),
            ],
        ),
    ]
