from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RememberMeAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetView, PasswordChangeDoneView, PasswordResetConfirmView, PasswordChangeView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe



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


from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_html_email(subject, template_name, context, recipient_list):
    html_message = render_to_string(template_name, context)
    plain_message = strip_tags(html_message)
   
    email = EmailMessage(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
    )

    email.attach(subject, html_message, "text/html")
    email.send()


# def confirm_account_mail(request):
#     subject = "Activate Account"
#     template_name = "confirm_account_mail.html"
#     context = {'context_variable': 'value'}
#     recipient_email = "artem.duda.shi.2022@lpnu.ua"

#     send_html_email(subject, template_name, context, [recipient_email])
#     return render(request, 'confirm_account_mail.html')

from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from email.mime.image import MIMEImage

def confirm_account_mail(request):
    subject = "Activate Account"
    template_name = "confirm_account_mail.html"
    context = {'context_variable': 'value'}
    recipient_email = "artem.duda.shi.2022@lpnu.ua"

    image_html = '<img src="cid:unique_image_id" alt="Chinese Dog Breeds">'
    
    context['image_html'] = image_html

    html_content = render_to_string(template_name, context)
    text_content = strip_tags(html_content)

    msg = EmailMultiAlternatives(subject, text_content, to=[recipient_email])
    msg.attach_alternative(html_content, "text/html")

    with open("./static/images/dog.png", "rb") as image_file:
        msg_img = MIMEImage(image_file.read())
        msg_img.add_header("Content-ID", "<unique_image_id>")
        msg.attach(msg_img)

    msg.send()

    return render(request, template_name, context)


def confirm_account(request):
    return render(request, 'confirm_account.html')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Password reset email has been sent. Check your inbox.'
        )
        return redirect(self.success_url)


class CustomPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Your password has been reset successfully. You can log in now.'
        )
        return redirect(self.success_url)

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Your password has been changed successfully.'
        )
        return redirect(self.success_url)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.user)

        messages.success(
            self.request, 'Your password has been reset. Please log in with your new password.'
        )

        return response

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    # success_url = reverse_lazy('home')

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.warning(self.request, 'There was an error changing your password. Please try again.')
        return response

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'There was an error resetting your password. Please make sure the link is valid and try again.')
        return response