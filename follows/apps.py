from django.apps import AppConfig

from common import EventBus
from .subscribers import UserCreatedSubscriber, UserSubscriber


class FollowsConfig(AppConfig):
    name = 'follows'

    def ready(self):
        EventBus.subscribe(UserCreatedSubscriber)
        EventBus.subscribe(UserSubscriber)
