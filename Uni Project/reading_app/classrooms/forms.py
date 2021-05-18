from django import forms
from . import models

class CreateClassroom(forms.ModelForm):
    class Meta:
        model = models.Classroom
        fields = ['name', 'code', 'upload']

# class AddFile(forms.ModelForm):
#     class Meta:
#         model = models.Classroom
#         fields = ['upload']

class JoinClass(forms.ModelForm):
    class Meta:
        model = models.Classroom_Student
        fields = ['code']