from django.contrib import admin
from django.urls import path, include
from watchlist_app.api.views import StreamPlatformSet, WatchListAV, WatchDetail, StreamPlatformAV, StreamPlatformDetails, ReviewList, ReviewDetail, ReviewCreate
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatformSet, basename='streamplatform')

urlpatterns = [
    path('', WatchListAV.as_view(), name='watch-list'),
    path('<int:id>', WatchDetail.as_view(), name='watch-details'),
    path('', include(router.urls)),

    # path('stream', StreamPlatformAV.as_view(), name='streamplatform-list'),
    # path('stream/<int:id>', StreamPlatformDetails.as_view(), name='streamplatform-detail'),

    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),


    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    # path('review', ReviewList.as_view(), name='review-list')
]


