from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("copyright/", views.copyright, name="copyright"),
    path("faq/", views.faq, name="faq"),
    path("login/", views.login, name="login"),
    path("market/", views.market, name="market"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("ranking/", views.ranking, name="ranking"),
    path("register/", views.register, name="register"),
    path("strategies/", views.strategies, name="strategies"),
]