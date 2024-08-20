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
    form = ExerciseForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        prompt = f"Generate a {form.cleaned_data['difficulty']} exercise in {form.cleaned_data['language']}"
        exercise = generate_exercise(prompt)
        return JsonResponse({'exercise': exercise})
    return render(request, 'users/generate_exercise.html', {'form': form})