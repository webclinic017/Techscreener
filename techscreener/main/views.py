from django.shortcuts import render
from .services.company_data import analysis_companies, strategies, stocks

# Create your views here.

def index(request):
    return render(request, "main/index.html", { 'pageIndex': 0, 'company': analysis_companies, 'indices': stocks, 'strategy': strategies })

def about(request):
    return render(request, "main/about.html", { 'pageIndex': 1 })

def market(request):
    return render(request, "main/market.html", { 'pageIndex': 2 })

def ranking(request):
    return render(request, "main/ranking.html", { 'pageIndex': 3 })

def portfolio(request):
    return render(request, "main/portfolio.html", { 'pageIndex': 4 })

def strategies(request):
    return render(request, "main/strategies.html", { 'pageIndex': 5 })

def faq(request):
    return render(request, "main/faq.html", { 'pageIndex': 6 })

def contact(request):
    return render(request, "main/contact.html", { 'pageIndex': 7 })

def copyright(request):
    return render(request, "main/copyright.html", {})

def login(request):
    return render(request, "main/login.html", {})

def register(request):
    return render(request, "main/register.html", {})

