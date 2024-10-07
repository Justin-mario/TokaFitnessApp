import unittest
from src.fitness_app.instructor import Instructor

class TestInstructor(unittest.TestCase):

    def test_instructor_creation(self):
        instructor = Instructor("Jimmy Cantadio", "jimmy@gmail.com", "123456", "Yoga")
        self.assertEqual(instructor.name, "Jimmy Cantadio")
        self.assertEqual(instructor.email, "jimmy@gmail.com")
        self.assertTrue(instructor.check_password("123456"))
        self.assertEqual(instructor.speciality, "Yoga")

    def test_instructor_inheritance(self):
        instructor = Instructor("John Smith", "john@gmail.com", "123456", "Pilates")
        self.assertTrue(hasattr(instructor, "name"))
        self.assertTrue(hasattr(instructor, "email"))

    def test_instructor_speciality_property(self):
        instructor = Instructor("Bob Johnson", "john@gmail.com", "123456", "Weightlifting")
        with self.assertRaises(AttributeError):
            instructor.speciality = "Cardio"

    def test_instructor_password(self):
        instructor = Instructor("Alice Brown", "alice@example.com", "alicepass", "Zumba")
        self.assertTrue(instructor.check_password("alicepass"))
        self.assertFalse(instructor.check_password("wrongpass"))

    def test_instructor_str_representation(self):
        instructor = Instructor("Alice Brown", "alice@example.com", "123456", "Zumba")
        self.assertEqual(str(instructor), "Instructor: Alice Brown, Speciality: Zumba")

if __name__ == '__main__':
    unittest.main()
