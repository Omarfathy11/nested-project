from django.contrib import admin
from django.urls import path
from .views import InstructorListView,CourseListView,Course_pk

urlpatterns = [
    path('instructors', InstructorListView.as_view()),
    path('courses', CourseListView.as_view()),
    path('course/generics/<int:pk>', Course_pk.as_view()),

]