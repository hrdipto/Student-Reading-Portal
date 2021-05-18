from django.urls import path
from . import views

app_name = 'classrooms'

urlpatterns = [
    path('', views.classroom_list, name="list"),
    path('join/', views.student_join, name="join"),
    path('create/', views.classroom_create, name="create"),
    path('<slug:code>/', views.classroom_detail, name="detail"),
]
