from django.urls import path
from .views import *
from BookApp import views

urlpatterns = [
    path('author/', views.AuthorList.as_view()),
    path('author/<int:pk>/', views.AuthorDetail.as_view()),
    path('book/', views.BookList.as_view()),
    path('book/<int:pk>/', views.BookDetail.as_view()),
]