from rest_framework  import serializers
from classroom.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['cid', 'name', 'homework', 'tid']