from django import forms
from .models import Person


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'password']


class PasswordResetRequest(forms.Form):
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if email:
            user = Person.objects.filter(email=email).first()

            if user is None:
                raise forms.ValidationError("Емейл не зареєстрований")

        return cleaned_data


class HandlePasswordReset(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Паролі не збігаються.")
        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = Person.objects.filter(email=email).first()

            if user is None or user.password != password:
                raise forms.ValidationError("Неправильний емеіл або пароль.")

        return cleaned_data
