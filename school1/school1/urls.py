"""school1 URL Configuration

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

from . import views
from school1 import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('uploadstudent/',views.uploadstudent,name='uploadstudents'),
    path('uploadteacher/',views.uploadteacher,name='uploadteachers'),
    path('uploadclass/',views.uploadclass,name='uploadclasss'),
    path('uploadattendance/',views.uploadattendance,name='uploadattendances'),
    path('updatestudent/<int:stud_id>',views.updatestudent),
    path('updateteacher/<int:tach_id>',views.updateteacher),
    path('updateclass/<int:class_id>',views.updateclass),
    path('updateattendance/<int:attendance_id>',views.updateattendance),
    path('deletestud/<int:stud_id>',views.deletestudent),
    path('deleteteach/<int:teach_id>',views.deleteteacher),
    path('deleteclass/<int:class_id>',views.deleteclass),
    path('deleteattendance/<int:attendance_id>',views.deleteattendance),
    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)