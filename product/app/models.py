from django.db import models

# Create your models here.
class Customer(models.Model):
    Customer_name=models.CharField(max_length=100)
    Address=models.CharField(max_length=200)
    Email=models.EmailField()
    def __str__(self):
        return self.Customer_name
    
class Product(models.Model):
    Picture=models.ImageField()
    Name=models.CharField(max_length=100)
    price=models.IntegerField()
    About=models.TextField()
    def __str__(self):
        return self.Name

class Order(models.Model):
    cname=models.ForeignKey(Customer,on_delete=models.CASCADE)
    pname=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
            
    