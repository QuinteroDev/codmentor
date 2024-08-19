from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    # Puedes añadir más rutas según las vistas que tengas en la app 'users'
]