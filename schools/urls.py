from django.urls import path
from . import views

app_name = 'schools'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('course/', views.CourseListView.as_view(),name='course_list'),
    path('course/<int:pk>/', views.CoureDetailView.as_view(), name='course_detail'),
    path('teachers/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
]