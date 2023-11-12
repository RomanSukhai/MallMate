from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RememberMeAuthenticationForm
from django.contrib.auth.views import LoginView


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Успішно створено акаунт для {email}')
            return redirect('login')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

# class RememberMeLoginView(LoginView):
#     form_class = RememberMeAuthenticationForm
#     template_name = 'login.html'

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.shortcuts import render
from .forms import RememberMeAuthenticationForm

class RememberMeLoginView(LoginView):
    form_class = RememberMeAuthenticationForm
    template_name = 'login.html'  # Вказуйте ваш шлях до шаблону відповідно

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me', False)

        # Виклик батьківського методу form_valid
        response = super().form_valid(form)

        if remember_me:
            # Встановлення терміну дії сесії на довгий період (наприклад, 30 днів)
            self.request.session.set_expiry(30 * 24 * 60 * 60)
        else:
            # Сесія закінчиться при закритті браузера
            self.request.session.set_expiry(0)

        return response

    def form_invalid(self, form):
        # Виклик батьківського методу form_invalid
        response = super().form_invalid(form)

        # Очистка терміну дії сесії при невірних облікових даних
        self.request.session.set_expiry(0)

        return response

@login_required()
def profile(request):
    return render(request, 'profile.html')
