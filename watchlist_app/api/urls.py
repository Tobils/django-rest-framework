from django.contrib import admin
from django.urls import path, include
from watchlist_app.api.views import movie_list, movie_details

urlpatterns = [
    path('', movie_list, name="movie-list"),
    path('<int:id>', movie_details, name="movie-details")
]
