from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RememberMeAuthenticationForm
from django.contrib.auth.views import LoginView


def register(request):
    error_messages = []

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account successfully created for {email}')
            return redirect('login')
        else:
            # Add error messages for each form field to a list
            for field, errors in form.errors.items():
                for error in errors:
                    # Check if the field has a label
                    field_label = form.fields.get(field, None)
                    if field_label:
                        error_messages.append(f"{field_label.label}: {error}")
                    else:
                        error_messages.append(error)

            # Display all error messages in a single alert
            if error_messages:
                messages.error(request, '\n'.join(error_messages), extra_tags='danger')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

# class RememberMeLoginView(LoginView):
#     form_class = RememberMeAuthenticationForm
#     template_name = 'login.html'

class RememberMeLoginView(LoginView):
    form_class = RememberMeAuthenticationForm
    template_name = 'login.html'  

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me', False)

        response = super().form_valid(form)

        if remember_me:
            self.request.session.set_expiry(30 * 24 * 60 * 60)
        else:
            self.request.session.set_expiry(0)

        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)

        for field, errors in form.errors.items():
            for error in errors:
                field_label = form.fields.get(field, None)
                if field_label:
                    messages.error(self.request, f"{field_label.label}: {error}", extra_tags='danger')
                else:
                    messages.error(self.request, error, extra_tags='danger')

        self.request.session.set_expiry(0)

        return response

@login_required()
def profile(request):
    return render(request, 'profile.html')


def confirm_account_mail(request):
    return render(request, 'confirm_account_mail.html')

def confirm_account(request):
    return render(request, 'confirm_account.html')