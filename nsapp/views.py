from django.shortcuts import render
from rest_framework import generics
from .models import course, Instructor
from .serializers import InstructorSerializer, CourseSerializer
# Create your views here.


class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class CourseListView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = course.objects.all()    
class Course_pk(generics.RetrieveUpdateDestroyAPIView):
     queryset = course.objects.all()
     serializer_class = CourseSerializer