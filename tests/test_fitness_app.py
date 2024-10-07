import unittest
from src.fitness_app.fitness_app import FitnessApp
from src.fitness_app.user import User
from src.fitness_app.instructor import Instructor
from src.fitness_app.workout_session import WorkoutSession

class TestFitnessApp(unittest.TestCase):

    def setUp(self):
        self.app = FitnessApp()

    def test_register_user(self):
        user = self.app.register_user("John Doe", "john@example.com", "password123")
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john@example.com")

    def test_register_instructor(self):
        instructor = self.app.register_instructor("Jane Smith", "jane@example.com", "password456", "Yoga")
        self.assertIsInstance(instructor, Instructor)
        self.assertEqual(instructor.name, "Jane Smith")
        self.assertEqual(instructor.email, "jane@example.com")
        self.assertEqual(instructor.speciality, "Yoga")

    def test_create_workout_session(self):
        instructor = self.app.register_instructor("Bob Johnson", "bob@example.com", "password789", "HIIT")
        session = self.app.create_workout_session("Morning HIIT", instructor)
        self.assertIsInstance(session, WorkoutSession)
        self.assertEqual(session.name, "Morning HIIT")
        self.assertEqual(session.instructor, instructor)

    def test_assign_user_to_session(self):
        user = self.app.register_user("Alice Brown", "alice@example.com", "password321")
        instructor = self.app.register_instructor("Charlie Davis", "charlie@example.com", "password654", "Pilates")
        session = self.app.create_workout_session("Evening Pilates", instructor)
        self.app.assign_user_to_session(user, session)
        self.assertIn(user, session.participants)

    def test_get_user_sessions(self):
        user = self.app.register_user("Eve Wilson", "eve@example.com", "password987")
        instructor = self.app.register_instructor("Frank Miller", "frank@example.com", "password135", "Zumba")
        session1 = self.app.create_workout_session("Zumba Class 1", instructor)
        session2 = self.app.create_workout_session("Zumba Class 2", instructor)
        self.app.assign_user_to_session(user, session1)
        self.app.assign_user_to_session(user, session2)
        user_sessions = self.app.get_user_sessions(user)
        self.assertEqual(len(user_sessions), 2)
        self.assertIn(session1, user_sessions)
        self.assertIn(session2, user_sessions)

    def test_get_instructor_sessions(self):
        instructor = self.app.register_instructor("Grace Lee", "grace@example.com", "password246", "Yoga")
        session1 = self.app.create_workout_session("Yoga Class 1", instructor)
        session2 = self.app.create_workout_session("Yoga Class 2", instructor)
        instructor_sessions = self.app.get_instructor_sessions(instructor)
        self.assertEqual(len(instructor_sessions), 2)
        self.assertIn(session1, instructor_sessions)
        self.assertIn(session2, instructor_sessions)

if __name__ == '__main__':
    unittest.main()
