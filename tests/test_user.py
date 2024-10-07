import unittest
from src.fitness_app.user import User

class TestUser(unittest.TestCase):

    def test_user_creation(self):
        user = User("Luke Shaw", "Luke@gmail.com", "123456")
        self.assertEqual(user.name, "Luke Shaw")
        self.assertEqual(user.email, "Luke@gmail.com")
        self.assertTrue(user.check_password("123456"))

    def test_user_name_property(self):
        user = User("Bobo Risky", "bob@gmail.com", "123456")
        with self.assertRaises(AttributeError):
            user.name = "New Name"

    def test_user_email_property(self):
        user = User("Bobo Risky", "bob@gmail.com", "123456")
        with self.assertRaises(AttributeError):
            user.email = "new_email@gmail.com"

if __name__ == '__main__':
    unittest.main()
