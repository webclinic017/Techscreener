from django.urls import path
from .views import RankingView, VisualizationView, StrategyView

urlpatterns = [
        path('ranking', RankingView.as_view()),
        path('visualization', VisualizationView.as_view()),
        path('strategy', StrategyView.as_view()),
]   
