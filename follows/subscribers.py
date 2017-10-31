from users.events import UserCreatedEvent, UserDeletedEvent

from .repositories import FollowsRepo


class UserCreatedSubscriber:
    subscribe_to = [UserCreatedEvent]

    @staticmethod
    def run(event):
        FollowsRepo.create_follow(event.user_id, event.user_id)
        print("Hello from follows! {}".format(event.user_id))


class UserSubscriber:
    subscribe_to = [UserDeletedEvent, UserCreatedEvent]

    @staticmethod
    def run(event):
        print("Hello from follows2! {}".format(event.user_id))
