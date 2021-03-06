from django.urls import path

from . import views

urlpatterns = [
path('customusers/', views.ListCustomeUsers.as_view()),
    path('customuser/<int:pk>/', views.DetailCustomeUsers.as_view()),

    path('colleges/', views.ListColleges.as_view()),
    path('college/<int:pk>/', views.DetailColleges.as_view()),

    path('students/', views.ListStudents.as_view()),
    path('student/<int:pk>/', views.DetailStudents.as_view()),

    path('professors/', views.ListProfessors.as_view()),
    path('professor/<int:pk>/', views.DetailProfessors.as_view()),
]