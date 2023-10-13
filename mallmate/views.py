from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .forms import RegistrationForm, LoginForm, PasswordResetRequest, HandlePasswordReset
from .models import Person, UserPasswordResetRequest
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
import random
import string

def generate_request_id(length=16):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def home(request):
    return render(request, "home.html")


def tima(request):
    return render(request, "tima.html", {'name': 'Timon'})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            if Person.objects.filter(email=email).exists():
                form.add_error('email', ValidationError('Ця пошта вже зареєстрована', code='duplicate_email'))
            else:
                user = form.save(commit=False)
                user.password = form.cleaned_data['password']
                user.save()
                return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def request_password_reset(request):
    if request.method == 'POST':
        form = PasswordResetRequest(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user_email = data['email']

            reset_request = UserPasswordResetRequest()
            reset_request.request_id = generate_request_id()
            reset_request.user_email = user_email

            reset_request.save()

            return render(request, 'password_reset_request_success.html', {'email': user_email})
    else:
        form = PasswordResetRequest()

    return render(request, 'request_password_request.html', {'form': form})

def handle_password_reset(request, request_id):
    try:
        req = UserPasswordResetRequest.objects.get(request_id=request_id)
    except UserPasswordResetRequest.DoesNotExist:
        raise Http404("Запит на скидання пароля не існує")

    if req.is_expired():
        raise Http404("Запит на скидання пароля прострочений")

    if request.method == 'POST':
        form = HandlePasswordReset(request.POST)

        if form.is_valid():
            user = Person.objects.get(email=req.user_email)
            user.password = form.cleaned_data['password']
            user.save()

            req.valid = False
            req.save()

            return render(request, 'home.html')
    else:
        form = HandlePasswordReset()

    return render(request, 'handle_password_reset.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('home')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
