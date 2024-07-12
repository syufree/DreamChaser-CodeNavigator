from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    username = models.CharField(verbose_name="用户名", max_length=255, default='')
    password = models.CharField(verbose_name="密码", max_length=255, default='')
    createTime = models.DateField(verbose_name="用户创建时间", auto_now_add=True)
    email = models.EmailField(verbose_name="邮箱", max_length=255, default="2935515548@qq.com")
    phone = models.CharField(verbose_name="电话号码", max_length=20, default="19993907551")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    moneyData = models.IntegerField(verbose_name="钱财", default=0)


    class Meta:
        db_table = 'user'






    
        # 知识点表
class Knowledge(models.Model):
    level = models.CharField(max_length=2)  
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  
    pointname = models.TextField(primary_key=True)  

    def __str__(self):
        return f"{self.pointname} (Level {self.level})"


# 测试题表
class questions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)   # type: ignore
    Level  =  models.ForeignKey(Knowledge, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)  # 题目
    answer = models.CharField(max_length=1)  # 答案

    def __str__(self):
        return self.question


# 课程表
class Course(models.Model):
    cname = models.CharField(max_length=100, primary_key=True)  # 课程名

    def __str__(self):
        return self.cname

# 用户学习状态表
class LearningStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 用户名
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # 所学课程
    level = models.ForeignKey(Knowledge, on_delete=models.CASCADE)  # 所学课程所处等级

    def __str__(self):
        return f"{self.user} - {self.course} - {self.level}"

        
        