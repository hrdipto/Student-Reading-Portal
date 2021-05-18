from django.db import models

# Create your models here.
class Teacher(models.Model):
    tid = models.IntegerField()
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)

    def __str__(self):
        return self.fname

class Student(models.Model):
    sid = models.IntegerField()
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)

    def __str__(self):
        return self.fname

class Course(models.Model):
    cid = models.IntegerField()
    name = models.CharField(max_length=200)
    homework = models.CharField(max_length=100)
    tid = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name