from django.contrib import admin
from django.urls import path, include
from watchlist_app.api.views import MovieList, MovieDetail

urlpatterns = [
    path('', MovieList.as_view(), name="movie-list"),
    path('<int:id>', MovieDetail.as_view(), name="movie-details")
]
