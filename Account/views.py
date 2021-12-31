from django.shortcuts import render


def signup(request):
    return render(request, "Account/signup.html")


def login(request):
    return render(request, "Account/login.html")
