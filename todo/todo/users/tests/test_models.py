from django.test import TestCase

from todo.users.tests.factories import UserFactory


class UserTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory(email='UserTestCase@gmail.com')

    def test_str(self):
        assert str(self.user) == f'{self.user.get_full_name()} (user {self.user.id})'
