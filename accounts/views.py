from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username atau password salah")

    return render(request, "accounts/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username sudah digunakan")
        else:
            User.objects.create_user(
                username=username,
                password=password
            )
            messages.success(request, "Registrasi berhasil, silakan login")
            return redirect("login")

    return render(request, "accounts/register.html")

def logout_view(request):
    logout(request)
    return redirect("login")

# Create your views here.
