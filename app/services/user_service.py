


def register_user(email, password):
    if "@" not in email:
        raise ValueError('Invalid email')