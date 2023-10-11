from django import forms
from .models import Person


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'password']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = Person.objects.filter(email=email).first()
            except Person.DoesNotExist:
                raise forms.ValidationError("Емеіл не знайдений або він не правильний")

            if user.password != password:
                raise forms.ValidationError("Неправильний пароль.")

        return cleaned_data
