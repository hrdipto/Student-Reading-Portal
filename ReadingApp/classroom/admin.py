from django.contrib import admin
from classroom.models import (Course, Teacher, Student)
# Register your models here.

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)