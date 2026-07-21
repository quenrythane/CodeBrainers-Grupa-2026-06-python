import pytest
from main import UserManager

@pytest.fixture
def user_manager():
    print("\nstart testu")
    return UserManager()  # user_manager = UserManager()


def test_add_user(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    assert user_manager.get_user("john_doe") == "john@example.com"


def test_add_duplicate_user(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("john_doe", "another@example.com")

def test_add_user_3(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    assert user_manager.get_user("john_doe") == "john@example.com"

def test_add_use_4(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    assert user_manager.get_user("john_doe") == "john@example.com"

def test_add_user_5(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    assert user_manager.get_user("john_doe") == "john@example.com"



