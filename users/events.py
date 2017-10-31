class UserCreatedEvent:
    def __init__(self, user_id):
        self.user_id = user_id


class UserDeletedEvent:
    def __init__(self, user_id):
        self.user_id = user_id
