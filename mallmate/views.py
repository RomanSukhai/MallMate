from django.shortcuts import render
from users.models import User
from django.contrib.auth.decorators import login_required


def landing(request):
    return render(request, 'landing.html')


@login_required()
def home(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

@login_required()
def profile(request):
    return render(request, 'profile.html')

def info(request):
    return render(request, 'info.html')

def map(request):
    return render(request, 'map.html')