def format_name(name: str) -> str:
    return name.strip().title()

def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email
