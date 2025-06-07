from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # Ruta raíz para el index
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('test/', views.test_page, name='test_page'),  # Aquí definimos la URL para el test

]
