# exercises/forms.py
from django import forms

class ExerciseForm(forms.Form):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('java', 'Java'),
        ('csharp', 'C#'),
        ('cpp', 'C++'),
        ('ruby', 'Ruby'),
        ('go', 'Go'),
        ('php', 'PHP'),
        ('swift', 'Swift'),
        ('typescript', 'TypeScript'),
        ('kotlin', 'Kotlin'),
        ('rust', 'Rust'),
    ]
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, label="Programming Language")
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES, label="Difficulty Level")