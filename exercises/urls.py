from django.urls import path
from .views import GenerateExerciseView # Vista que muestra la página de generación de ejercicios

urlpatterns = [
    path('generate-exercise/', GenerateExerciseView.as_view(), name='generate-exercise'),  # Ruta de generación de ejercicios
]