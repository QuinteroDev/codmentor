# exercises/views.py
from django.views.generic.edit import FormView
from .forms import ExerciseForm
from .utils import generate_exercise
from django.shortcuts import render

class GenerateExerciseView(FormView):
    template_name = 'exercises/generate_exercise.html'
    form_class = ExerciseForm

    def form_valid(self, form):
        language = form.cleaned_data['language']
        difficulty = form.cleaned_data['difficulty']
        
        # Llamada a la función para generar el ejercicio
        exercise = generate_exercise(language, difficulty)

        # Renderizar el template con el ejercicio generado
        return render(self.request, self.template_name, {
            'form': form,
            'exercise': exercise
        })