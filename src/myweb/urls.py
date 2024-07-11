"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path as url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url('again/', views.again, name='again'),
    url('index/', views.index, name='index'),
    url('lan/', views.lan, name='lan'),
    url('login/', views.login, name='login'),
    url('register/', views.register, name='register'),
    url('python/', views.python, name='python'),
    url('C++/', views.Cpp, name='C++'),
    url('css/', views.css, name='css'),
    url('end/', views.end, name='end'),
    url('ret/', views.ret, name='ret')
    #path('',views.again,name='again'),
]
