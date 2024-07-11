from django.shortcuts import render

# Create your views here.
#主要的函数，所有函数中要求有需求request

#定义函数1
def index(request):
    return render(request,"index.html",{})#返回一个响应HTTPresponse

def home(request):
    print("enter home")
    return render(request,"index.html",{})
# src/myweb/views.py

def again(request):
    return render(request,"index.html",{})

def lan(request):
    return render(request, 'lan.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def python(request):
    return render(request, 'python.html')

def Cpp(request):
    return render(request, 'C++.html')

def css(request):
    return render(request, 'css.html')

def end(request):
    return render(request, 'end.html')

def ret(request):
    return render(request, 'return.html')



