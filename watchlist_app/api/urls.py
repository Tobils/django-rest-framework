from django.contrib import admin
from django.urls import path, include
from watchlist_app.api.views import WatchListAV, WatchDetail, StreamPlatformAV, StreamPlatformDetails

urlpatterns = [
    path('', WatchListAV.as_view(), name="movie-list"),
    path('<int:id>', WatchDetail.as_view(), name="movie-details"),
    path('stream', StreamPlatformAV.as_view(), name="stream-list"),
    path('stream/<int:id>', StreamPlatformDetails.as_view(), name="stream-details")
]
