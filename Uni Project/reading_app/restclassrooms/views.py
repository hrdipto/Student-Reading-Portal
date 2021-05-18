from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse

from .serializers import (
    # addSerializer,
    listSerializer,
    classroomStudentListSerializer,
    joinSerializer,
    listByTeacherSerializer,
    classroomStudentListByStudentSerializer,
    # listCategorySerializer,
    # showSerializer,
)

from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.response import Response

from classrooms.models import Classroom
from classrooms.models import Classroom_Student

from rest_framework.permissions import (
    IsAuthenticated,
)

from .permissions import IsOwnerOrReadOnly


from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication

class ClassroomListAPIView(ListAPIView):
    serializer_class = listSerializer
    queryset = Classroom.objects.all()

class ClassroomListByTeaher(ListAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
	serializer_class = listByTeacherSerializer

	def get_queryset(self, *args, **kwargs):
		return Classroom.objects.all().filter(teacher=self.request.user)





class ClassroomStudentAPIView(ListAPIView):
    serializer_class = classroomStudentListSerializer
    queryset = Classroom_Student.objects.all()

class ClassroomStudentListByStudent(ListAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
	serializer_class = classroomStudentListByStudentSerializer

	def get_queryset(self, *args, **kwargs):
		return Classroom_Student.objects.all().filter(student=self.request.user)






class ClassroomJoin(CreateAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	serializer_class = joinSerializer
	queryset = Classroom_Student.objects.all()

	def perform_create(self, serializer):
		serializer.save(student = self.request.user)