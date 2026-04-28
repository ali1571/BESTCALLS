# bestcallproj/bestcallapp/apps.py

from django.apps import AppConfig


class BestcallappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'

    # Update this name to match the full path
    name = 'bestcallproj.bestcallapp'