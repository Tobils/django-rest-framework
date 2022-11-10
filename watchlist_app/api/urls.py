from django.contrib import admin
from django.urls import path, include
from watchlist_app.api.views import WatchListAV, WatchDetail, StreamPlatformAV, StreamPlatformDetails, ReviewList, ReviewDetail

urlpatterns = [
    path('', WatchListAV.as_view(), name='watch-list'),
    path('<int:id>', WatchDetail.as_view(), name='watch-details'),
    path('stream', StreamPlatformAV.as_view(), name='streamplatform-list'),
    path('stream/<int:id>', StreamPlatformDetails.as_view(), name='streamplatform-detail'),

    # path('stream/<int:id>/review', StreamPlatformDetails.as_view(), name='streamplatform-detail'),
    # path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),


    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    path('review', ReviewList.as_view(), name='review-list')
]
