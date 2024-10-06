from src.fitness_app.user import User
from src.fitness_app.instructor import Instructor

class WorkoutSession:
    def __init__(self, name, instructor, max_capacity=None):
        self._name = name
        self._instructor = instructor
        self._max_capacity = max_capacity
        self._participants = set()


    @property
    def instructor(self):
        return self._instructor


    @property
    def name(self):
        return self._name

    @property
    def participants(self):
        return list(self._participants)

    def add_participant(self, user):
        if not isinstance(user, User):
            raise TypeError('Participant must be of type User')
        if self._max_capacity and len(self._participants) >= self._max_capacity:
            raise ValueError('Maximum capacity reached')
        self._participants.add(user)

    def remove_participant(self, users):
        self._participants.discard(users)

    def __str__(self):
        return f"Workout Session: {self.name}, Instructor: {self.instructor.name}"


