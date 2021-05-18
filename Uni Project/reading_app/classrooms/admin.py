from django.contrib import admin
from .models import Classroom, Classroom_Student

myModels = [Classroom, Classroom_Student]

admin.site.register(myModels)
