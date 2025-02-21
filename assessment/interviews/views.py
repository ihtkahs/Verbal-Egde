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
            return redirect('dashboard')  # Redirect to a dashboard/home page after signup
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

def practice_view(request):
    questions = Question.objects.all()  # Fetch all questions
    return render(request, 'interviews/practice.html', {'questions': questions})

@csrf_exempt  # Temporarily disable CSRF for testing
def save_audio(request):
    if request.method == 'POST':
        user = request.user
        question_id = request.POST.get('question_id')
        audio_data = request.POST.get('audio_file')

        if not audio_data:
            return HttpResponse("No audio file received", status=400)

        question = Question.objects.get(id=question_id)
        
        # Decode base64 audio data
        format, audio_str = audio_data.split(';base64,')
        ext = format.split('/')[-1]  # Get file extension
        audio_bytes = base64.b64decode(audio_str)

        # Save audio file
        audio_file = ContentFile(audio_bytes, name=f"{user.username}_Q{question_id}.{ext}")
        AudioResponse.objects.create(user=user, question=question, audio_file=audio_file)

        return redirect('practice') 

