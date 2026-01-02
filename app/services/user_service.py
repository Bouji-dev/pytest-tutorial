
def validate_email(email):
    if not email or "@" not in email:
        raise ValueError("Invalid email")
    
def validate_password(password):
    if len(password) < 8:
        raise ValueError('Password is too short')

def validate_email_exists(email, user_repository):
    if user_repository.email_exists(email):
        raise ValueError('Email already exists')

def register_user(email, password, user_repository):
    validate_email(email)
    validate_password(password)
    validate_email_exists(email, user_repository)
    

