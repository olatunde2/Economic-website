from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Teacher, Student, Course, Event

# Create your views here.

class HomeView(ListView):
    template_name = 'schools/home.html'
    context_object_name = 'events'
    queryset = Event.objects.order_by('-date')[:3]


class CourseListView(ListView):
    model = Course
    template_name = 'schools/course_list.html'
    context_object_name = 'courses'


class CoureDetailView(DetailView):
    model = Course
    template_name = 'schools/course_detail.html'
    context_object_name = 'courses'


class TeacherListView(ListView):
    model = Teacher
    template_name = 'schools/teacher_list.html'
    context_object_name = 'teachers'


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'schools/teacher_detail.html'
    context_object_name = 'teachers'


class StudentListView(ListView):
    model = Student
    template_name = 'schools/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'schools/student_detail.html'
    context_object_name = 'students'

class EventListView(ListView):
    model = Event
    template_name = 'schools/event_list.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    template_name = 'schools/event_detail.html'
    context_object_name = 'events'