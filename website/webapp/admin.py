from django.contrib import admin
from .models import Event, Testimony, Latest_news, Photo

class EventAdmin(admin.ModelAdmin):
        list_display = ('title', 'created_at', 'event_date', 'image')
        search_fields = ('title', 'content')
        list_filter = ('created_at',)

admin.site.register(Event, EventAdmin)

class TestimonyAdmin(admin.ModelAdmin):
        list_display = ('title', 'created_at', 'testimony_date', 'image')
        search_fields = ('title', 'content')
        list_filter = ('created_at',)

admin.site.register(Testimony, TestimonyAdmin)

class Latest_newsAdmin(admin.ModelAdmin):
        list_display = ('title', 'created_at', 'news_date')
        search_fields = ('title', 'content')
        list_filter = ('created_at',)

admin.site.register(Latest_news, Latest_newsAdmin)

class PhotoAdmin(admin.ModelAdmin):
        list_display = ('title', 'created_at', 'photo_date', 'image')
        list_filter = ('created_at',)

admin.site.register(Photo, PhotoAdmin)