from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
    ExerciseForm
)
from .models import Profile
from .openai_client import generate_exercise
from django.views.decorators.csrf import csrf_exempt
import subprocess

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')

def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Account created for {form.cleaned_data["username"]}! You can now log in.')
        return redirect('login')
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    return render(request, 'users/profile.html', {'u_form': u_form, 'p_form': p_form})

def generate_exercise_view(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data['language']
            difficulty = form.cleaned_data['difficulty']
            prompt = f"Generate a {difficulty} exercise in {language}"
            exercise = generate_exercise(prompt)
            
            # Renderiza la plantilla con el ejercicio y el editor
            return render(request, 'users/generate_exercise.html', {
                'form': form,
                'exercise': exercise,
            })
    else:
        form = ExerciseForm()

    return render(request, 'users/generate_exercise.html', {'form': form})

@csrf_exempt  # Exenta de la verificación CSRF solo para propósitos de prueba
def run_code_view(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        language = request.POST.get('language', 'python')

        try:
            # Dependiendo del lenguaje seleccionado, ejecuta el código
            if language == 'python':
                result = subprocess.run(
                    ['python3', '-c', code],
                    capture_output=True,
                    text=True
                )
            else:
                return JsonResponse({'error': 'Unsupported language'}, status=400)

            return JsonResponse({'output': result.stdout, 'error': result.stderr})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)