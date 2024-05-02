import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage: generate a password with default length of 12 characters
print("Generated password:", generate_password())

# Example usage: generate a password with custom length of 16 characters
print("Generated password (length 16):", generate_password(16))
