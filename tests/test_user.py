import pytest
from src.fitness_app.user import User

def test_user_creation():
    user = User("Luke Shaw", "Luke@gmail.com", "123456")
    assert user.name == "Luke Shaw"
    assert user.email == "Luke@gmail.com"
    assert user.password == "123456"

def test_user_name_property():
    user = User("Bobo Risky", "bob@gmail.com", "123456")
    with pytest.raises(AttributeError):
        user.name = "New Name"

def test_user_email_property():
    user = User("Bobo Risky", "bob@gmail.com", "123456")
    with pytest.raises(AttributeError):
        user.email = "new_email@gmail.com"