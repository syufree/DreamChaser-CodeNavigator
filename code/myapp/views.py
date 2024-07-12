from django.shortcuts import render

# Create your views here.
import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models import Q




from django.shortcuts import render, HttpResponse, redirect
from django import forms
from myapp import models
from myapp.utils.bootstrap import BootStrapForm
from myapp.models import User
from django.contrib import messages
from myapp.utils.pagination import Pagination

# Create your views here.
class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={'class': 'custom-input'}),
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )

    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=False
    )


class RegisterForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )

    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True),
        required=True
    )


def login(request):
    """ 登录 """
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'loginn.html', {'form': form})

    form = LoginForm(data=request.POST)

    if form.is_valid():
        # 去数据库校验用户名和密码是否正确，获取用户对象或None
        admin_object = models.User.objects.filter(username=form.cleaned_data['username'],
                                                  password=form.cleaned_data['password']).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'loginn.html', {'form': form})

        # 用户名和密码正确
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        request.session.set_expiry(60 * 60 * 24 * 7)  # 设置session过期时间为7天
        return redirect("/myapp/index/")
    return render(request, 'loginn.html', {'form': form})


def logout(request):
    """ 注销 """
    request.session.clear()
    return redirect('/myapp/login/')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            # 检查密码和确认密码是否一致
            if password != confirm_password:
                form.add_error("confirm_password", "密码与确认密码不匹配")
                return render(request, 'register.html', {'form': form})  # 返回注册页面，重新填写表单
            # 检查用户名是否已存在
            if User.objects.filter(username=username).exists():
                form.add_error("username", "用户名已存在")
                return render(request, 'register.html', {'form': form})  # 返回注册页面，重新填写表单
            # 创建新用户
            user = User.objects.create(username=username, password=password)

            user.save()
            messages.success(request, '注册成功，请登录')
            return redirect('/myapp/login/')  # 注册成功后重定向到登录页面
        else:
            messages.error(request, '请正确填写表单')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def index(request):
    return render(request,'index.html')

def end(request):
    return render(request,'end.html')

def html(request):
    return render(request,'html.html')

def css(request):
    return render(request,'css.html')

def cpp(request):
    return render(request,'cpp.html')
#cpp测试页面
def javas(request):

    return render(request,'js.html')
def python(request):
    return render(request,'python.html')

def pythons(request):
    return render(request,'pythons.html')

def cssl(request):

    return render(request,'cssl.html')

def jss(request):

    return render(request,'jss.html')

def project(request):

    return render(request,'C++.html')

def myself(request):#自己等级的页面，个人信息

    return render(request,'myself.html')


from django.shortcuts import render, redirect
from .models import User, Course, Knowledge, LearningStatus, questions
def start_learning(request):
    if request.method == 'POST':
        user = User.objects.get(mail=request.user.mail)
        course_name = request.POST.get('course_name')
        course = Course.objects.get(sname=course_name)
        
        initial_status = LearningStatus(user=user, course=course, level=Knowledge.objects.get(level="1"))
        initial_status.save()
        
        return redirect('course_detail', course_name=course.sname)
    else:
        courses = Course.objects.all()
        return render(request, 'start_learning.html', {'courses': courses})


def course_detail(request, course_name):
    course = Course.objects.get(sname=course_name)
    user_status = LearningStatus.objects.get(user=request.user, course=course)
    knowledge_point = Knowledge.objects.filter(level=user_status.level.level).first()
    
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        user_answer = request.POST.get('answer')
        question = questions.objects.get(id=question_id)
        
        if user_answer == question.answer:
            next_level = Knowledge.objects.filter(level=str(int(user_status.level.level)+1)).first()
            user_status.level = next_level
            user_status.save()
            correct_answer = True
        else:
            correct_answer = False
        
        return render(request, 'course_detail.html', {'course': course, 'knowledge_point': knowledge_point, 'question': question, 'correct_answer': correct_answer})
    
    question = questions.objects.filter(level=knowledge_point.level).order_by('?').first()
    return render(request, 'course_detail.html', {'course': course, 'knowledge_point': knowledge_point, 'question': question})
    