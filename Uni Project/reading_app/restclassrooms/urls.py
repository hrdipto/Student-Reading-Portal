from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ClassroomListAPIView.as_view(), name="restclassroom-list"),
    path('listbyteacher/', views.ClassroomListByTeaher.as_view(), name="restclassroom-list-teacher"),
    path('join/', views.ClassroomJoin.as_view(), name="restclassroom-join"),
    path('classroomstudentlist/', views.ClassroomStudentAPIView.as_view(), name="restclassroom-studentlist"),
    path('classroomsbystudent/', views.ClassroomStudentListByStudent.as_view(), name="restclassroom-studentlist-student"),
]
