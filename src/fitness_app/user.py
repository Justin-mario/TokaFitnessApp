import bcrypt

class User:
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email


    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self._password_hash)

