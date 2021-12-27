from django.urls import path
from engine.views import Ranking

urlpatterns = [
    path('', Ranking.as_view()),
]
