from django.contrib import admin
from django.urls import path, include
from myweb import views

#定义路径
urlpatterns = [
   #path('',include('myweb.urls')),
    path('',views.home,name='home'),
     path('again/', views.again, name='again'),
     path('lan/', views.lan, name='lan'),
     path('ret/', views.ret, name='ret'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    #path('admin/', admin.site.urls),
]
