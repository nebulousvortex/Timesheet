from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, TextInput, PasswordInput


class LoginUserForm(AuthenticationForm):
    username = CharField(label="Логин", widget=TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Логин'
    }))
    password = CharField(label="Пароль", widget=PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Пароль'
    }))

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Логин'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-input',
                'placeholder': 'Пароль'
            }),
        }

class RegisterUserForm(UserCreationForm):
    username = CharField(label="Логин", widget=TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Логин'
    }))
    password1 = CharField(label="Пароль", widget=PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Пароль'
    }))
    password2 = CharField(label='Повтор пароля', widget=PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Повтор пароля'
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Логин'
            }),
            "password1": PasswordInput(attrs={
                'class': 'form-input',
                'placeholder': 'Пароль'
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-input',
                'placeholder': 'Подтверждение пароля'
            }),
        }