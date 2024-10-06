from src.fitness_app.user import User

class Instructor(User):
    def __init__(self, name, email, password, speciality):
        super().__init__(name, email, password)
        self._speciality = speciality


    @property
    def speciality(self):
        return self._speciality

    def __str__(self):
        return f"Instructor: {self.name}, Speciality: {self.speciality}"