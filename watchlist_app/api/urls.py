from django.contrib import admin
from django.urls import path, include
from watchlist_app.api.views import WatchListAV, WatchDetail, StreamPlatformAV, StreamPlatformDetails

urlpatterns = [
    path('', WatchListAV.as_view(), name='watch-list'),
    path('<int:id>', WatchDetail.as_view(), name='watch-details'),
    path('stream', StreamPlatformAV.as_view(), name='streamplatform-list'),
    path('stream/<int:id>', StreamPlatformDetails.as_view(), name='streamplatform-detail')
]
