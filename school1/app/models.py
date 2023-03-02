from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=100)
    age=models.IntegerField()
    enrollment_date=models.DateField()
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.student_name
    
class Teacher(models.Model):
    teacher_name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.teacher_name
    
        
class Class (models.Model):
    class_name=models.CharField(max_length=100)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    students=models.ManyToManyField(Student)
    def __str__(self):
        return self.class_name 
    
class Attendance (models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    class_name=models.ForeignKey(Class,on_delete=models.CASCADE)
    date=models.DateField()
    present=models.BooleanField()
        
       