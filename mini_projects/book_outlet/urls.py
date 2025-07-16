from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.book_details, name='book_details'),
    path('', views.index, name='index'),
]