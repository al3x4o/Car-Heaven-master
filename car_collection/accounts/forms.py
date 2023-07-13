from django import forms
from django.contrib.auth import authenticate
from django.forms import TextInput, NumberInput, PasswordInput

from .models import Profile
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'age', 'password1', 'password2')
        help_texts = {
            'username': None,
            'email': None,
            'age': None,
            'password1': None,
            'password2': None,
        }
        widgets = {
            "username": TextInput(attrs={'placeholder': 'Username', 'autocomplete': 'off'}),
            "first_name": TextInput(attrs={'placeholder': 'First Name', 'autocomplete': 'off'}),
            "last_name": TextInput(attrs={'placeholder': 'Last Name(Optional)', 'autocomplete': 'off'}),
            "email": TextInput(attrs={'placeholder': 'Email', 'autocomplete': 'off'}),
            "age": NumberInput(attrs={'placeholder': 'Age', 'autocomplete': 'off'}),
            "password1": PasswordInput(
                attrs={'placeholder': 'Password', 'autocomplete': 'off', 'data-toggle': 'password'}),
            "password2": PasswordInput(
                attrs={'placeholder': 'Password(Confirm)', 'autocomplete': 'off', 'data-toggle': 'password'}),
        }


class SignInForm(auth_forms.AuthenticationForm):
    username = forms.CharField()
    fields = ('username', 'password')
    widgets = {
        "username": TextInput(attrs={'placeholder': 'Username', 'autocomplete': 'off'}),
        "password": PasswordInput(
            attrs={'placeholder': 'Password', 'autocomplete': 'off', 'data-toggle': 'password'}),
    }

# al3x4o2
# password234
