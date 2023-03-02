
from django.shortcuts import render,redirect
from .models import Customer,Product,Order
from .forms import newcustomer,neworder,newproduct
from django.template import loader
from django.http import HttpResponse
# Create your views here.


def index(request):
    a=Customer.objects.all()
    b=Product.objects.all()
    c=Order.objects.all()
    
    return render (request,'main.html',{'customerdetail':a,'productdetail':b,'orderdetail':c}) 

    
def uploadcustomer(request):
    abc=newcustomer()
    if request.method == 'POST':
        abc=newcustomer(request.POST ,request.FILES )
        if abc.is_valid():
            abc.save()    
            return redirect('index')
        else:
            HttpResponse ('data is wrong')
    
    else:
        
        return render (request,'customerupload.html',{'upload_customer':abc})        
    
def uploadproduct(request):
    abc=newproduct()
    if request.method == 'POST':
        abc=newproduct(request.POST ,request.FILES )
        if abc.is_valid():
            abc.save()    
            return redirect('index')
        else:
            HttpResponse ('data is wrong')
    
    else:
               
        return render (request,'productupload.html',{'upload_product':abc})     

def uploadorder(request):
    abc=neworder()
    if request.method == 'POST':
        abc=neworder(request.POST ,request.FILES )
        if abc.is_valid():
            abc.save()    
            return redirect('index')
        else:
            HttpResponse ('data is wrong')
    
    else:
        
        return render (request,'orderupload.html',{'upload_order':abc})            
           
        
    
def updatecustomer(request,cust_id):
    cust_id=int(cust_id)
    try:
        abc=Customer.objects.get(id=cust_id)
        
    except Customer.DoesNotExist:
        return redirect ('index')
        
    xyz=newcustomer(request.POST or None ,instance=abc)
    if xyz.is_valid():
        
        xyz.save()
        return redirect('index')
         
    return render(request,'customerupload.html',{'upload_customer':xyz})        
    
def updateproduct(request,prod_id):
    prod_id=int(prod_id)
    try:
        abc=Product.objects.get(id=prod_id)
        
    except Product.DoesNotExist:
        return redirect ('index')
        
    xyz=newproduct(request.POST or None ,instance=abc)
    if xyz.is_valid():
        
        xyz.save()
        return redirect('index')
         
    return render(request,'productupload.html',{'upload_product':xyz})    

def updateorder(request,order_id):
    order_id=int(order_id)
    try:
        abc=Order.objects.get(id=order_id)
        
    except Order.DoesNotExist:
        return redirect ('index')
        
    xyz=neworder(request.POST or None ,instance=abc)
    if xyz.is_valid():
        
        xyz.save()
        return redirect('index')
         
    return render(request,'orderupload.html',{'upload_order':xyz})  


        
def deletecustomer(request,cust_id):
    cust_id=int(cust_id)
    try:
        abc=Customer.objects.get(id=cust_id)
    except Customer.DoesNotExist:
        return redirect('index')
    abc.delete()
    return redirect ('index')
        
            
def deleteproduct(request,prod_id):
    prod_id=int(prod_id)
    try:
        abc=Product.objects.get(id=prod_id)
    except Product.DoesNotExist:
        return redirect('index')
    abc.delete()
    return redirect ('index')
                    
def deleteorder(request,order_id):
    order_id=int(order_id)
    try:
        abc=Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return redirect('index')
    abc.delete()
    return redirect ('index')

