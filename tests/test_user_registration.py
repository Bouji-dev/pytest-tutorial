import sys
sys.path.append('.')

import pytest
from unittest.mock import Mock
from app.services.user_service import register_user

class FakeUserRepository:
    def __init__(self, exists=False):
        self._exists = exists

    def email_exists(self, email):
        return self._exists

@pytest.fixture
def duplicate_email_repo():
    return FakeUserRepository(exists=True)

@pytest.fixture
def new_email_repo():
    return FakeUserRepository(exists=False)

def test_register_user_with_invalid_email_should_fail(duplicate_email_repo):
    with pytest.raises(ValueError):
        register_user('invalid-email', '123456789', duplicate_email_repo)

def test_register_user_with_invalid_password_should_fail(duplicate_email_repo):
    with pytest.raises(ValueError):
        register_user('valid@emial', '123', duplicate_email_repo)

def test_register_user_with_exists_email_should_fail(duplicate_email_repo):
    with pytest.raises(ValueError):
        register_user('user@test.com', '12345678', duplicate_email_repo)

def test_register_user_with_new_email_should_pass(new_email_repo):
    register_user('user@test.com', '12345678', new_email_repo)

def test_register_user_success_calls_repository():
    repo = Mock()
    repo.email_exists.return_value = False

    register_user('user@test.com', '12345678', repo)

    repo.email_exists.assert_called_once_with('user@test.com')


def test_register_user_duplicate_email_stops_flow():
    repo = Mock()
    repo.email_exists.return_value = True

    with pytest.raises(ValueError):
        register_user('user@test.com', '12345678', repo)

    repo.email_exists.assert_called_once_with('user@test.com')
    assert repo.method_calls == [('email_exists', ('user@test.com',), {})]