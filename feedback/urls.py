# feedback/urls.py
from django.urls import path
from .views import FeedbackView

urlpatterns = [
    path('run-code/', FeedbackView.as_view(), name='run_code'),  # Ruta para ejecutar código
]