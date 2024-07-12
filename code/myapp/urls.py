from django.urls import path, re_path
from myapp import views

urlpatterns = [
    # 登录，注册
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logOut'),
    path('index/', views.index),
    path('html/', views.html),
    path('css/',views.css),
    path('javas/',views.javas),
    path('python/',views.python),
    path('pythons/',views.pythons),
    path('cssl/',views.cssl),
    path('project/',views.project),
    path('cpp/',views.cpp),
    path('jss/',views.jss),
    path('end/',views.end),
    path('myself/',views.myself)
]
