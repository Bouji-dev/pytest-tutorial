import pytest
from app.services.user_service import register_user


def test_register_user_with_invalid_email_should_fail():
    with pytest.raises(ValueError):
        register_user('invalid-email', '123456789')