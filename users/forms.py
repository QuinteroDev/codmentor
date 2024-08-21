from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'location']

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
        ('beginner', 'Beginner'),
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
        ('expert', 'Expert'),
    ]


    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES)
