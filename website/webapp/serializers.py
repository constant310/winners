from rest_framework import serializers
from .models import Event, Testimony, Photo, Latest_news

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimony
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class LatestNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Latest_news
        fields = '__all__'