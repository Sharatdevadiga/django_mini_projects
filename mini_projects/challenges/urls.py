from django.urls import path
from . import views

app_name = 'challenges'

urlpatterns = [
    path("", views.index, name="index"),      
    path("<int:month>", views.monthly_challenge_by_number, name="month-challenge-by-number"),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]