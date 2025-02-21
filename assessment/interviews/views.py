from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.http import HttpResponse, JsonResponse
import os
import base64
from .forms import SignupForm
from .models import Question, AudioResponse  

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after signup
    else:
        form = SignupForm()
    return render(request, 'interviews/signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'interviews/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    return render(request, 'interviews/dashboard.html')

@login_required
def practice_view(request):
    questions = Question.objects.all()
    return render(request, 'interviews/practice_home.html', {'questions': questions})

@login_required
def dashboard_home(request):
    if request.headers.get('HX-Request'):
        return render(request, 'interviews/dashboard_home.html')
    return render(request, 'interviews/dashboard.html')

@login_required
def practice(request):
    if request.headers.get('HX-Request'):
        return render(request, 'interviews/practice.html')
    return render(request, 'interviews/dashboard.html')

@login_required
def responses(request):
    if request.headers.get('HX-Request'):
        return render(request, 'interviews/responses.html')
    return render(request, 'interviews/dashboard.html')

@login_required
def performance(request):
    if request.headers.get('HX-Request'):
        return render(request, 'interviews/performance.html')
    return render(request, 'interviews/dashboard.html')

@login_required
def settings_home(request):
    if request.headers.get('HX-Request'):
        return render(request, 'interviews/settings_home.html')
    return render(request, 'interviews/dashboard.html')

@csrf_exempt  # Temporarily disable CSRF for testing
def save_audio(request):
    if request.method == 'POST':
        user = request.user
        question_ids = request.POST.getlist('question_id')

        for question_id in question_ids:
            audio_file = request.FILES.get(f'audio_file_{question_id}')

            if not audio_file:
                return HttpResponse(f"No audio file received for question {question_id}", status=400)

            question = Question.objects.get(id=question_id)
            AudioResponse.objects.create(user=user, question=question, audio_file=audio_file)

        return redirect('practice_home')

    return HttpResponse("Invalid request", status=400)