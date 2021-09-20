from django.shortcuts import render, redirect
from services.company_data import analysis_companies, Strategies, stocks

# Create your views here.

def index(request):
    return render(request, "main/index.html", { 'pageIndex': 0, 'company': analysis_companies, 'indices': stocks, 'strategy': Strategies })

def about(request):
    return render(request, "main/about.html", { 'pageIndex': 1 })

def market(request):
    if not hasattr(request, 'username'):
        response = redirect('/login?message=Login to view the page')
        return response
    return render(request, "main/market.html", { 'pageIndex': 2, 'company': analysis_companies })

def ranking(request):
    if not hasattr(request, 'username'):
        response = redirect('/login?message=Login to view the page')
        return response
    return render(request, "main/ranking.html", { 'pageIndex': 3 })

def portfolio(request):
    if not hasattr(request, 'username'):
        response = redirect('/login?message=Login to view the page')
        return response
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

