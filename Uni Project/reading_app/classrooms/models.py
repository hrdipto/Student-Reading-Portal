from django.db import models
from django.contrib.auth import get_user_model as user_model
User = user_model()
from accounts.models import Account

def generate_filename(self, filename):
    url = "%s/%s" % (self.code, filename)
    return url

class Classroom(models.Model):
    code = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to=generate_filename, blank=False, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return 'code: ' + self.code + ' | ' + 'name: ' + self.name 

    def justshow(self):
        return 'This is class of ' + self.name[:3]


class Classroom_Student(models.Model):
    code = models.CharField(max_length=6)
    student = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return 'class_code:' + self.code + ' | ' + 'student_username:' + self.student.username