from django import forms
from .models import Student,Teacher,Class,Attendance


class newstudent(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        
        
class newteacher(forms.ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'
        
        
class newclass(forms.ModelForm):
    class Meta:
        model=Class
        fields='__all__'
        
class newattendance(forms.ModelForm):
    class Meta:
        model=Attendance
        fields='__all__'