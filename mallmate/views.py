from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm, PasswordResetRequest
from .models import Person
from django.shortcuts import get_object_or_404
from .models import UserPasswordResetRequest
from django.contrib.auth.models import User
from django.utils import timezone
import random
import string

def generate_request_id(length=24):
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
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})



from django.contrib.auth.models import User

from django.contrib.auth.models import User

def password_reset_request(request):
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

    return render(request, 'password_reset_request.html', {'form': form})

def handle_password_reset_request(request, request_id):
    return HttpResponse(request_id)

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
