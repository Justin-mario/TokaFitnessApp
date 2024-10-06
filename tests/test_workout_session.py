import pytest
from src.fitness_app.user import User
from src.fitness_app.instructor import Instructor
from src.fitness_app.workout_session import WorkoutSession

@pytest.fixture
def sample_instructor():
    return Instructor("Jane Doe", "jane@example.com", "password123", "Yoga")

@pytest.fixture
def sample_user():
    return User("John Smith", "john@example.com", "password456")

def test_workout_session_creation(sample_instructor):
    session = WorkoutSession("Morning Yoga", sample_instructor)
    assert session.name == "Morning Yoga"
    assert session.instructor == sample_instructor
    assert len(session.participants) == 0

def test_add_participant(sample_instructor, sample_user):
    session = WorkoutSession("Evening Pilates", sample_instructor)
    session.add_participant(sample_user)
    assert len(session.participants) == 1
    assert sample_user in session.participants

def test_remove_participant(sample_instructor, sample_user):
    session = WorkoutSession("HIIT Class", sample_instructor)
    session.add_participant(sample_user)
    session.remove_participant(sample_user)
    assert len(session.participants) == 0

def test_add_duplicate_participant(sample_instructor, sample_user):
    session = WorkoutSession("Spin Class", sample_instructor)
    session.add_participant(sample_user)
    session.add_participant(sample_user)
    assert len(session.participants) == 1

def test_session_capacity(sample_instructor):
    session = WorkoutSession("Limited Class", sample_instructor, max_capacity=2)
    user1 = User("User1", "user1@example.com", "pass1")
    user2 = User("User2", "user2@example.com", "pass2")
    user3 = User("User3", "user3@example.com", "pass3")

    session.add_participant(user1)
    session.add_participant(user2)
    with pytest.raises(ValueError):
        session.add_participant(user3)

def test_session_str_representation(sample_instructor):
    session = WorkoutSession("Zumba Party", sample_instructor)
    assert str(session) == "Workout Session: Zumba Party, Instructor: Jane Doe"