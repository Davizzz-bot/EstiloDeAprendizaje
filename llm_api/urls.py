from django.urls import path
from .views import *

urlpatterns = [
    path('api/student-recommendations/', student_recommendations, name='student_recommendations'),
    path('api/teacher-recommendations/', teacher_recommendations, name='teacher_recommendations'),
    path('api/save-test-results/', save_test_results, name='save_test_results'),
    path("api/calcular_promedio_por_grupo", calcular_promedio_por_grupo, name="calcular_promedio_por_grupo"),
]
