import unittest
from app.models import User


class UserModelTestCase(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password='bull')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('bull'))
        self.assertTrue(self.new_user.verify_password('bull'))

    # def test_password_salts_are_random('self'):
    #     u = User(password='cat')
    #     u2 = User(password='cat')
    #     self.assertTrue(u.password_hash != u2.password_hash)
