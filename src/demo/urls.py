from django.contrib import admin
from django.urls import path, include
from myweb import views

#定义路径
urlpatterns = [
    path('',include('myweb.urls')),
    path('admin/', admin.site.urls),
]
