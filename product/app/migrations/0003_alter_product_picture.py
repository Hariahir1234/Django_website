# Generated by Django 4.1.4 on 2023-01-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
