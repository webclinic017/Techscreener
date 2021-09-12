from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "main/index.html", {})

def about(request):
    return render(request, "main/about.html", {})

def contact(request):
    return render(request, "main/contact.html", {})

def copyright(request):
    return render(request, "main/copyright.html", {})

def faq(request):
    return render(request, "main/faq.html", {})

def login(request):
    return render(request, "main/login.html", {})

def market(request):
    return render(request, "main/market.html", {})

def portfolio(request):
    return render(request, "main/portfolio.html", {})

def ranking(request):
    return render(request, "main/ranking.html", {})

def register(request):
    return render(request, "main/register.html", {})

def strategies(request):
    return render(request, "main/strategies.html", {})