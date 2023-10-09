from django import forms


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='Ім\'я', max_length=30)
    last_name = forms.CharField(label='Прізвище', max_length=30)
    email = forms.EmailField(label='Електронна пошта')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.EmailField(label='Ім\'я користувача ')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)