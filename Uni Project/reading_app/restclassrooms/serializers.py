from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
)
from classrooms.models import Classroom
from classrooms.models import Classroom_Student


class listSerializer(ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            'id',
            'name',
            'code',
            'date',
            'upload',
            'teacher',
        ]

class listByTeacherSerializer(ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            'id',
            'name',
            'code',
            'date',
            'upload',
            'teacher',
        ]

class classroomStudentListSerializer(ModelSerializer):
    class Meta:
        model = Classroom_Student
        fields = [
            'id',
            'code',
            'student',
        ]

class classroomStudentListByStudentSerializer(ModelSerializer):
    class Meta:
        model = Classroom_Student
        fields = [
            'id',
            'code',
            'student',
        ]

class joinSerializer(ModelSerializer):
	class Meta:
		model = Classroom_Student
		fields = [
			'code',
		]