from django.urls import path,include
# from watchlistApp.api import views
from watchlistApp.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', views.stream, basename='views')


urlpatterns=[
    path('list/',views.totalWatchLists.as_view(),name='movie-list'),
    path('<int:pk>/',views.watchListById.as_view(),name='movie-details'),

    # path('stream/list/',views.streamList.as_view(),name='stream-list'),
    # path('stream/<int:pk>/',views.streamListById.as_view(),name='stream-details'),

    # path('rating/list/',views.reviewList.as_view(),name='review-list'),
    path('review/<int:pk>/',views.reviewListById.as_view(),name='review-details'),
    path('<int:pk>/review/',views.reviewList.as_view(),name='review-list'),
    path('<int:pk>/review-create/',views.reviewCreate.as_view(),name='review-create'),
    path('',include(router.urls))
]