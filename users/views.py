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
from .openai_client import generate_exercise, generate_openai_feedback
from django.views.decorators.csrf import csrf_exempt
import subprocess
import time
import resource  # Usado para medir el uso de recursos en sistemas Unix

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
            exercise = generate_exercise(language, difficulty)
            return render(request, 'users/generate_exercise.html', {
                'form': form,
                'exercise': exercise
            })
    else:
        form = ExerciseForm()

    return render(request, 'users/generate_exercise.html', {'form': form})

def run_code_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        language = request.POST.get('language')
        exercise_description = request.POST.get('exercise_description')
        expected_output = "Expected output based on the exercise"  # Define this properly based on the exercise.

        if code and language and exercise_description:
            evaluation_result = evaluate_code(
                code,
                expected_output,
                language,
                exercise_description
            )
            return JsonResponse(evaluation_result)
        else:
            return JsonResponse({'error': 'Code, language, or exercise description not provided'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
def run_user_code(user_code):
    try:
        # Guardar el código del usuario en un archivo temporal
        with open("temp_user_code.py", "w") as code_file:
            code_file.write(user_code)
        
        # Ejecutar el código y capturar la salida
        process = subprocess.run(["python3", "temp_user_code.py"], capture_output=True, text=True, timeout=5)
        
        # Verificar si hubo errores durante la ejecución
        if process.stderr:
            return process.stderr.strip()
        
        # Devolver la salida estándar si no hubo errores
        return process.stdout.strip()
    
    except subprocess.TimeoutExpired:
        return "Error: El código tomó demasiado tiempo en ejecutarse y fue terminado."
    except Exception as e:
        return f"Error: {str(e)}"
    
def evaluate_code(user_code, expected_output, language, exercise_description):
    try:
        # Ejecutar el código del usuario
        output = run_user_code(user_code)
        
        # Verificar si el output es correcto
        is_correct = output == expected_output

        # Generar el feedback utilizando OpenAI
        openai_feedback = generate_openai_feedback(user_code, expected_output, exercise_description)
        
        return {
            "feedback": openai_feedback
        }
    except Exception as e:
        return {"feedback": f"Error: {str(e)}"}