from src.fitness_app.user import User
from src.fitness_app.instructor import Instructor
from src.fitness_app.workout_session import WorkoutSession

class FitnessApp:
    def __init__(self):
        self._users = []
        self._instructors = []
        self._sessions = []

    def register_user(self, name, email, password):
        user = User(name, email, password)
        self._users.append(user)
        return user

    def register_instructor(self, name, email, password, speciality):
        instructor = Instructor(name, email, password, speciality)
        self._instructors.append(instructor)
        return instructor

    def create_workout_session(self, name, instructor):
        if instructor not in self._instructors:
            raise ValueError("Instructor not registered in the app")
        session = WorkoutSession(name, instructor)
        self._sessions.append(session)
        return session

    def assign_user_to_session(self, user, session):
        if user not in self._users:
            raise ValueError("User not registered in the app")
        if session not in self._sessions:
            raise ValueError("Session not found in the app")
        session.add_participant(user)

    def get_user_sessions(self, user):
        if user not in self._users:
            raise ValueError("User not registered in the app")
        return [session for session in self._sessions if user in session.participants]

    def get_instructor_sessions(self, instructor):
        if instructor not in self._instructors:
            raise ValueError("Instructor not registered in the app")
        return [session for session in self._sessions if session.instructor == instructor]