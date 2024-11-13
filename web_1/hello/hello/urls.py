"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import re_path
from firstapp import views
from django.views.generic import TemplateView

urlpatterns = [
 path('', views.index),
 path('about/', TemplateView.as_view(template_name="firstapp/about.html")),
 path('contact/', TemplateView.as_view(template_name="firstapp/contact.html",
    extra_context={"work": "Разработка программных продуктов"})),
 path('', views.index, name='index'),
 path('about/', views.about, name='about'),
 path('contact/', views.contact, name='contact'),
 path('my_form/', views.my_form, name='my_form'),
 path('my_form/edit_form/<int:id>/', views.edit_form, name='edit_form'),
 path('my_form/delete/<int:id>/', views.delete),
#  path('form_up_img/', views.form_up_img, name='form_up_img'),
#  path('form_up_img/delete_img/<int:id>/', views.delete_img),
 path('form_up_pdf/', views.form_up_pdf, name='form_up_pdf'),
 path('form_up_pdf/delete_pdf/<int:id>/', views.delete_pdf),  
 path('form_up_video/', views.form_up_video, name='form_up_video'),
 path('form_up_video/delete_video/<int:id>/', views.delete_video),
 path('form_up_audio/', views.form_up_audio, name='form_up_audio'),
 path('form_up_audio/delete_audio/<int:id>/', views.delete_audio),
 

]



