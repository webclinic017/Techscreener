from django.urls import path
from .views import CreateView, EditView, FetchView

urlpatterns = [
        path('create', CreateView.as_view()),
        path('edit', EditView.as_view()),
        path('all', FetchView.as_view()),
]   