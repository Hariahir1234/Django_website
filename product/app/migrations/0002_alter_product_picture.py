# Generated by Django 4.1.4 on 2023-01-29 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Picture',
            field=models.ImageField(upload_to='shop/images'),
        ),
    ]
