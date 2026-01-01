def register_user(email, password, user_repository):
    if "@" not in email:
        raise ValueError('Invalid email')
    
    if len(password) < 8:
        raise ValueError('Password is too short')
    
    if user_repository.email_exists(email):
        raise ValueError('Email already exists')
