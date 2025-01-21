# backend/blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Event URLs
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),

    # Testimony URLs
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/<int:pk>/', views.TestimonyDetailView.as_view(), name='testimony_detail'),

    # Latest News URLs
    path('latest-news/', views.LatestNewsListView.as_view(), name='latest_news_list'),
    path('latest-news/<int:pk>/', views.LatestNewsDetailView.as_view(), name='latest_news_detail'),

    # Photo URLs
    path('photos/', views.PhotoListView.as_view(), name='photo_list'),
   
]
