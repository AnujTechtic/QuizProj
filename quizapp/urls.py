from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('questionView/<str:pk>/', views.questionView, name='questionView'),
    path('studentRegister/<str:pk>/', views.studentRegister, name='studentRegister'),
    path('quizView', views.quizView, name='quizView'),
    path('quizCreate', views.quizCreate, name='quizCreate'),
    path('facultyLogin', views.facultyLogin, name='facultyLogin'),
    path('questionCreate', views.questionCreate, name='questionCreate'),
]