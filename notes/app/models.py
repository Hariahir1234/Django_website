from django.db import models

# Create your models here.
class notes(models.Model):
    Title=models.CharField(max_length=100)
    Describe=models.TextField()
    
    