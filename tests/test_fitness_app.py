import pytest
from src.fitness_app.fitness_app import FitnessApp
from src.fitness_app.user import User
from src.fitness_app.instructor import Instructor
from src.fitness_app.workout_session import WorkoutSession

@pytest.fixture
def app():
    return FitnessApp()

def test_register_user(app):
    user = app.register_user("John Doe", "john@example.com", "password123")
    assert isinstance(user, User)
    assert user.name == "John Doe"
    assert user.email == "john@example.com"

def test_register_instructor(app):
    instructor = app.register_instructor("Jane Smith", "jane@example.com", "password456", "Yoga")
    assert isinstance(instructor, Instructor)
    assert instructor.name == "Jane Smith"
    assert instructor.email == "jane@example.com"
    assert instructor.speciality == "Yoga"

def test_create_workout_session(app):
    instructor = app.register_instructor("Bob Johnson", "bob@example.com", "password789", "HIIT")
    session = app.create_workout_session("Morning HIIT", instructor)
    assert isinstance(session, WorkoutSession)
    assert session.name == "Morning HIIT"
    assert session.instructor == instructor

def test_assign_user_to_session(app):
    user = app.register_user("Alice Brown", "alice@example.com", "password321")
    instructor = app.register_instructor("Charlie Davis", "charlie@example.com", "password654", "Pilates")
    session = app.create_workout_session("Evening Pilates", instructor)
    app.assign_user_to_session(user, session)
    assert user in session.participants

def test_get_user_sessions(app):
    user = app.register_user("Eve Wilson", "eve@example.com", "password987")
    instructor = app.register_instructor("Frank Miller", "frank@example.com", "password135", "Zumba")
    session1 = app.create_workout_session("Zumba Class 1", instructor)
    session2 = app.create_workout_session("Zumba Class 2", instructor)
    app.assign_user_to_session(user, session1)
    app.assign_user_to_session(user, session2)
    user_sessions = app.get_user_sessions(user)
    assert len(user_sessions) == 2
    assert session1 in user_sessions
    assert session2 in user_sessions

def test_get_instructor_sessions(app):
    instructor = app.register_instructor("Grace Lee", "grace@example.com", "password246", "Yoga")
    session1 = app.create_workout_session("Yoga Class 1", instructor)
    session2 = app.create_workout_session("Yoga Class 2", instructor)
    instructor_sessions = app.get_instructor_sessions(instructor)
    assert len(instructor_sessions) == 2
    assert session1 in instructor_sessions
    assert session2 in instructor_sessions