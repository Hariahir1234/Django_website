"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app import views
from product.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('uploadcustomer/',views.uploadcustomer,name='uploadcustomers'),
    path('uploadproduct/',views.uploadproduct,name='uploadproducts'),
    path('uploadorder/',views.uploadorder,name='uploadorders'),

    path('updatecust/<int:cust_id>',views.updatecustomer),
    path('updateprod/<int:prod_id>',views.updateproduct),
    path('updateorder/<int:order_id>',views.updateorder),
   
    path('deletecust/<int:cust_id>',views.deletecustomer),
    path('deleteprod/<int:prod_id>',views.deleteproduct),
    path('deleteorder/<int:order_id>',views.deleteorder),
    
] 
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
