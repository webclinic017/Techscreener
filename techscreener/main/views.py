from django.shortcuts import render

# Create your views here.

def index(response):
    return render(response, "main/index.html", {})

def form(response):
    return render(response, "main/form.html", {})

def table(response):
    return render(response, "main/table.html", {})

def login(response):
    return render(response, "main/login.html", {})

def register(response):
    return render(response, "main/register.html", {})