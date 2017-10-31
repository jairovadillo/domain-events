from django.apps import AppConfig


class FollowsConfig(AppConfig):
    name = 'follows'

    def ready(self):
        # DANGER! IF THIS IMPORT IS REMOVED LISTENERS WON'T WORK! NEVER USE AUTOFORMAT HERE!
        from . import listeners
