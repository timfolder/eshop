from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    groups = forms.ChoiceField(choices=[("customer", "Customer"), ("seller", "Seller")], required=True)
    class Meta():
        model = User
        fields = ["username", "email", "password1", "password2", "groups"]