# Generated by Django 5.0.3 on 2025-01-20 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_event_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='slug',
        ),
    ]
