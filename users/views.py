from rest_framework.views import APIView, status, Response

from common import EventBus
from .events import UserCreatedEvent, UserDeletedEvent


class UsersView(APIView):
    def post(self, request):
        # Following code should go into the interactor:
        print("UsersView called")

        print("Pre send event 1")
        EventBus.trigger(UserCreatedEvent(user_id=1))
        print("Post send event 1")

        print("Pre send event 2")
        EventBus.trigger(UserDeletedEvent(user_id=4))
        print("Post send event 2")

        return Response(status=status.HTTP_204_NO_CONTENT)
