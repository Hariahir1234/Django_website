
from django.shortcuts import render,redirect
from .models import Student,Teacher,Class,Attendance
from .forms import newattendance,newstudent,newclass,newteacher
from django.template import loader
from django.http import HttpResponse
# Create your views here.


def index(request):
    a=Student.objects.all()
    b=Teacher.objects.all()
    c=Class.objects.all()
    d=Attendance.objects.all()
    return render (request,'main.html',{'studentdetail':a,'teacherdetail':b,'classdetail':c,'attendancedetail':d}) 

    
def uploadstudent(request):
    abc=newstudent()
    if request.method == 'POST':
        abc=newstudent(request.POST ,request.FILES )
        if abc.is_valid():
            abc.save()    
            return redirect('index')
        else:
            HttpResponse ('data is wrong')
    
    else:
        
        return render (request,'uploadstudent.html',{'upload_student':abc})        
    
def uploadteacher(request):
    abc=newteacher()
    if request.method == 'POST':
        abc=newteacher(request.POST ,request.FILES )
        if abc.is_valid():
            abc.save()    
            return redirect('index')
        else:
            HttpResponse ('data is wrong')
    
    else:
               
        return render (request,'uploadteacher.html',{'upload_teacher':abc})     

def uploadclass(request):
    abc=newclass()
    if request.method == 'POST':
        abc=newclass(request.POST ,request.FILES )
        if abc.is_valid():
            abc.save()    
            return redirect('index')
        else:
            HttpResponse ('data is wrong')
    
    else:
        
        return render (request,'uploadclass.html',{'upload_class':abc})            

def uploadattendance(request):
    abc=newattendance()
    if request.method == 'POST':
        abc=newattendance(request.POST ,request.FILES )
        if abc.is_valid():
            abc.save()    
            return redirect('index')
        else:
            HttpResponse ('data is wrong')
    
    else:
        
        return render (request,'uploadattendance.html',{'upload_attendance':abc})            
        
    
def updatestudent(request,stud_id):
    stud_id=int(stud_id)
    try:
        abc=Student.objects.get(id=stud_id)
        
    except Student.DoesNotExist:
        return redirect ('index')
        
    xyz=newstudent(request.POST or None ,instance=abc)
    if xyz.is_valid():
        
        xyz.save()
        return redirect('index')
         
    return render(request,'uploadstudent.html',{'upload_student':xyz})        
    
def updateteacher(request,teach_id):
    teach_id=int(teach_id)
    try:
        abc=Teacher.objects.get(id=teach_id)
        
    except Teacher.DoesNotExist:
        return redirect ('index')
        
    xyz=newteacher(request.POST or None ,instance=abc)
    if xyz.is_valid():
        
        xyz.save()
        return redirect('index')
         
    return render(request,'uploadteacher.html',{'upload_teacher':xyz})    

def updateclass(request,class_id):
    class_id=int(class_id)
    try:
        abc=Class.objects.get(id=class_id)
        
    except Class.DoesNotExist:
        return redirect ('index')
        
    xyz=newclass(request.POST or None ,instance=abc)
    if xyz.is_valid():
        
        xyz.save()
        return redirect('index')
         
    return render(request,'uploadclass.html',{'upload_class':xyz})  

def updateattendance(request,attendance_id):
    attendance_id=int(attendance_id)
    try:
        abc=Attendance.objects.get(id=attendance_id)
        
    except Attendance.DoesNotExist:
        return redirect ('index')
        
    xyz=newattendance(request.POST or None ,instance=abc)
    if xyz.is_valid():
        
        xyz.save()
        return redirect('index')
         
    return render(request,'uploadattendance.html',{'upload_attendance':xyz})  



        
def deletestudent(request,stud_id):
    stud_id=int(stud_id)
    try:
        abc=Student.objects.get(id=stud_id)
    except Student.DoesNotExist:
        return redirect('index')
    abc.delete()
    return redirect ('index')
        
            
def deleteteacher(request,teach_id):
    teach_id=int(teach_id)
    try:
        abc=Teacher.objects.get(id=teach_id)
    except Teacher.DoesNotExist:
        return redirect('index')
    abc.delete()
    return redirect ('index')
                    
def deleteclass(request,class_id):
    class_id=int(class_id)
    try:
        abc=Class.objects.get(id=class_id)
    except Class.DoesNotExist:
        return redirect('index')
    abc.delete()
    return redirect ('index')

def deleteattendance(request,attendance_id):
    attendance_id=int(attendance_id)
    try:
        abc=Attendance.objects.get(id=attendance_id)
    except Attendance.DoesNotExist:
        return redirect('index')
    abc.delete()
    return redirect ('index')