from django.shortcuts import render
from django.http import JsonResponse
from .forms import ExerciseForm
from .openai_client import generate_exercise, generate_openai_feedback
from django.views.decorators.csrf import csrf_exempt
import subprocess
import json
from django.contrib import messages


def generate_exercise_view(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data['language']
            difficulty = form.cleaned_data['difficulty']
            exercise = generate_exercise(language, difficulty)
            return render(request, 'generate_exercise.html', {
                'form': form,
                'exercise': exercise
            })
        else:
            messages.error(request, "Please select both a programming language and a difficulty level.")
    else:
        form = ExerciseForm()
    return render(request, 'generate_exercise.html', {'form': form})

@csrf_exempt
def run_code_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            code = data.get('code')
            exercise_description = data.get('exercise_description')

            if not code or not exercise_description:
                return JsonResponse({'error': 'Code or exercise description missing'}, status=400)

            # Aquí manejamos la ejecución del código del usuario
            result = run_user_code(code)

            # Generar feedback usando OpenAI
            feedback = generate_openai_feedback(user_code=code, expected_output=result, exercise_description=exercise_description)

            return JsonResponse({'feedback': feedback})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def run_user_code(user_code):
    try:
        # Guardar el código del usuario en un archivo temporal
        with open("temp_user_code.py", "w") as code_file:
            code_file.write(user_code)
        
        # Ejecutar el código y capturar la salida
        process = subprocess.run(["python3", "temp_user_code.py"], capture_output=True, text=True, timeout=5)
        
        if process.stderr:
            return process.stderr.strip()
        
        return process.stdout.strip()
    except subprocess.TimeoutExpired:
        return "Error: Code spend too much time and stopped."
    except Exception as e:
        return f"Error: {str(e)}"