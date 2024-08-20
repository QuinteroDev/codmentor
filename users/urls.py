from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('generate-exercise/', views.generate_exercise_view, name='generate_exercise'), 
    path('run-code/', views.run_code_view, name='run_code'),  # Nueva ruta para ejecutar código
]