from django import forms
from .models import Order,Customer,Product



class newcustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields='__all__'
        
class newproduct(forms.ModelForm):
    class Meta:
        model = Product
        fields='__all__'       
  
class neworder(forms.ModelForm):
    class Meta:
        model =Order
        fields='__all__'
