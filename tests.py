from django.test import TestCase

from follows.repositories import FollowsRepo


class UsersView(TestCase):
    def test_trigger_events(self):
        response = self.client.post('/users/', data={})

        assert len(FollowsRepo.all()) == 1
