


def register_user(email, password):
    if "@" not in email:
        raise ValueError('Invalid email')
    if len(password) < 8:
        raise ValueError('Password is too short')