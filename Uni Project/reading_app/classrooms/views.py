from django.shortcuts import render, redirect
from .models import Classroom, Classroom_Student
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url="/accounts/login/")
def classroom_list(request):
    classrooms = Classroom.objects.all().order_by('date')
    codes_student = Classroom_Student.objects.all().filter(student = request.user )
    return render(request, 'classrooms/classroom_list.html', {'classrooms': classrooms, 'codes_student': codes_student})

@login_required(login_url="/accounts/login/")
def classroom_detail(request, code):
    #return HttpResponse(code)
    classroom = Classroom.objects.get(code=code)
    return render(request, 'classrooms/classroom_detail.html', {'classroom': classroom})

@login_required(login_url="/accounts/login/")
def classroom_create(request):
    if request.method == 'POST':
        form = forms.CreateClassroom(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.teacher = request.user
            instance.save()
            return redirect('classrooms:list')
    else:
        form = forms.CreateClassroom()
    return render(request, 'classrooms/classroom_create.html', {'form': form})


@login_required(login_url="/accounts/login/")
def student_join(request):
    if request.method == 'POST':
        form = forms.JoinClass(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.student = request.user
            try:
                exists = Classroom.objects.get(code=instance.code)
                if exists:
                    instance.save()
            except:
                return redirect('classrooms:list')
            return redirect('classrooms:list')
    else:
        form = forms.JoinClass()
    return render(request, 'classrooms/student_join.html', {'form': form})

# @login_required(login_url="/accounts/login/")
# def classroom_add_file(request):
#     if request.method == 'POST':
#         classroom = Classroom.objects.get(teacher=request.user)
#         form = forms.AddFile(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.code = classroom.code
#             instance.save()
#             return redirect('classrooms:list')
#     else:
#         form = forms.AddFile()
#     return render(request, 'classrooms/classroom_addfile.html', {'form': form})
