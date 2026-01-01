import sys
sys.path.append('.')

import pytest
from app.services.user_service import register_user

class FakeUserRepository:
    def email_exists(self, email):
        return True
    
# repo = FakeUserRepository()

@pytest.fixture
def duplicate_email_repo():
    return FakeUserRepository()


def test_register_user_with_invalid_email_should_fail(duplicate_email_repo):
    with pytest.raises(ValueError):
        register_user('invalid-email', '123456789', duplicate_email_repo)

def test_register_user_with_invalid_password_should_fail(duplicate_email_repo):
    with pytest.raises(ValueError):
        register_user('valid@emial', '123', duplicate_email_repo)

def test_register_user_with_exists_email_should_fail(duplicate_email_repo):
    with pytest.raises(ValueError):
        register_user('user@test.com', '12345678', duplicate_email_repo)

