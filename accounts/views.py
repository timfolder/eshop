from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.conf import settings

class LoginPage(View):
    def get(self, request):
        return render(request, 'accounts/login.html')
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or Password are incorrect")
            return redirect("login")

class RegisterPage(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")
    def form_valid(self, form):
        print(form.instance.username)
        email = EmailMessage("Welcome to our Chairshop", f"Welcome, {form.instance.username}!", settings.EMAIL_HOST_USER, to=[form.instance.email])
        email.send(fail_silently = False)
        return super().form_valid(form)

        
def logoutview(request):
    logout(request)
    return redirect("home")


        
