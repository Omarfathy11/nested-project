from .models import course, Instructor
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
   # instrucotr = InstructorSerializer(read_only =True, many=True)
    class Meta:
        model = course
        fields = '__all__'


class InstructorSerializer(serializers.ModelSerializer):
   courses = CourseSerializer(many=True, read_only =True)
   class Meta:
            model = Instructor
            fields = '__all__'


