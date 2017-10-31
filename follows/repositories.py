class FollowsRepo:
    _follows = []

    @classmethod
    def create_follow(cls, source_user_id, target_user_id):
        cls._follows.append((source_user_id, target_user_id))

    @classmethod
    def all(cls):
        return cls._follows
