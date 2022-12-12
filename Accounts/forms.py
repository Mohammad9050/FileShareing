from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    # username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)

    # password1 = forms.PasswordInput()
    # password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
