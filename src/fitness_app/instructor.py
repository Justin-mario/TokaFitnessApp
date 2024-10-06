import bcrypt
from src.fitness_app.user import User

class Instructor(User):
    def __init__(self, name, email, password, speciality):
        super().__init__(name, email, password)
        self._password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self._speciality = speciality


    @property
    def speciality(self):
        return self._speciality

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self._password_hash)

    def __str__(self):
        return f"Instructor: {self.name}, Speciality: {self.speciality}"