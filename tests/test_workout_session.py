import unittest
from src.fitness_app.user import User
from src.fitness_app.instructor import Instructor
from src.fitness_app.workout_session import WorkoutSession

class TestFitnessApp(unittest.TestCase):

    def setUp(self):
        self.sample_instructor = Instructor("Jane Doe", "jane@example.com", "password123", "Yoga")
        self.sample_user = User("John Smith", "john@example.com", "password456")

    def test_workout_session_creation(self):
        session = WorkoutSession("Morning Yoga", self.sample_instructor)
        self.assertEqual(session.name, "Morning Yoga")
        self.assertEqual(session.instructor, self.sample_instructor)
        self.assertEqual(len(session.participants), 0)

    def test_add_participant(self):
        session = WorkoutSession("Evening Pilates", self.sample_instructor)
        session.add_participant(self.sample_user)
        self.assertEqual(len(session.participants), 1)
        self.assertIn(self.sample_user, session.participants)

    def test_remove_participant(self):
        session = WorkoutSession("HIIT Class", self.sample_instructor)
        session.add_participant(self.sample_user)
        session.remove_participant(self.sample_user)
        self.assertEqual(len(session.participants), 0)

    def test_add_duplicate_participant(self):
        session = WorkoutSession("Spin Class", self.sample_instructor)
        session.add_participant(self.sample_user)
        session.add_participant(self.sample_user)
        self.assertEqual(len(session.participants), 1)

    def test_session_capacity(self):
        session = WorkoutSession("Limited Class", self.sample_instructor, max_capacity=2)
        user1 = User("User1", "user1@example.com", "pass1")
        user2 = User("User2", "user2@example.com", "pass2")
        user3 = User("User3", "user3@example.com", "pass3")

        session.add_participant(user1)
        session.add_participant(user2)
        with self.assertRaises(ValueError):
            session.add_participant(user3)

    def test_session_str_representation(self):
        session = WorkoutSession("Zumba Party", self.sample_instructor)
        self.assertEqual(str(session), "Workout Session: Zumba Party, Instructor: Jane Doe")

if __name__ == '__main__':
    unittest.main()
