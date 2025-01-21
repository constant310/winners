# backend/blog/views.py

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Event, Photo, Testimony, Latest_news
from .serializers import EventSerializer, PhotoSerializer, TestimonySerializer, LatestNewsSerializer

class StandardResultsSetPagination(PageNumberPagination):
    """
    Custom pagination class to control the number of events per page.
    Adjust 'page_size' as needed.
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('-event_date')  # Orders events by latest date
    serializer_class = EventSerializer
    pagination_class = StandardResultsSetPagination

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TestimonyListView(generics.ListCreateAPIView):
    queryset = Testimony.objects.all().order_by('-testimony_date')
    serializer_class = TestimonySerializer
    pagination_class = StandardResultsSetPagination

class TestimonyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer

class LatestNewsListView(generics.ListCreateAPIView):
    queryset = Latest_news.objects.all().order_by('-news_date')
    serializer_class = LatestNewsSerializer
    pagination_class = StandardResultsSetPagination

class LatestNewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Latest_news.objects.all()
    serializer_class = LatestNewsSerializer

class PhotoListView(generics.ListCreateAPIView):
    queryset = Photo.objects.all().order_by('-photo_date')
    serializer_class = PhotoSerializer
    pagination_class = StandardResultsSetPagination

