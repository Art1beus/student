from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('student/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('exams/edit/<int:student_id>/', views.edit_exams, name='edit_exams'),
]
