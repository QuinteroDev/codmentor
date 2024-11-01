# exercises/views.py
from django.views.generic.edit import FormView
from .forms import ExerciseForm
from .utils import generate_exercise
from django.shortcuts import render
from django.http import JsonResponse

class GenerateExerciseView(FormView):
    template_name = 'exercises/generate_exercise.html'
    form_class = ExerciseForm

    def form_valid(self, form):
        language = form.cleaned_data['language']
        difficulty = form.cleaned_data['difficulty']
        
        # Llamada a OpenAI para generar el ejercicio
        exercise = generate_exercise(language, difficulty)

        # Renderizamos el ejercicio generado, sin incluir feedback o editor de código aún
        return render(self.request, self.template_name, {
            'form': form,
            'exercise': exercise
        })