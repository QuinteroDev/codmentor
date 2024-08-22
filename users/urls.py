from django.urls import path
from . import views

urlpatterns = [
    path('generate-exercise/', views.generate_exercise_view, name='generate_exercise'), 
    path('run-code/', views.run_code_view, name='run_code'),  # Nueva ruta para ejecutar código
]