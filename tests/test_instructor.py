import pytest
from src.fitness_app.instructor import Instructor

def test_instructor_creation():
    instructor = Instructor("Jimmy Cantadio", "jimmy@gmail.com", "123456", "Yoga" )
    assert instructor.name == "Jimmy Cantadio"
    assert instructor.email == "jimmy@gmail.com"
    assert instructor.password == "123456"
    assert instructor.speciality == "Yoga"

def test_instructor_inheritance():
    instructor =  Instructor("John Smith",  "john@gmail.com", "123456", "Pilates")
    assert hasattr(instructor, "name")
    assert hasattr(instructor, "email")

def test_instructor_speciality_property():
    instructor =  Instructor("Bob Johnson", "john@gmail.com", "123456", "Weightlifting" )
    with pytest.raises(AttributeError):
        instructor.speciality = "Cardio"


def test_instructor_str_representation():
    instructor = Instructor("Alice Brown", "alice@example.com", "123456","Zumba")
    assert str(instructor) == "Instructor: Alice Brown, Speciality: Zumba"