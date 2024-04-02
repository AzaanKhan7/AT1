import secrets
import string

def generate_secret_key(length=4):
    # Define the characters to choose from for the secret key
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random secret key of specified length
    secret_key = ''.join(secrets.choice(characters) for _ in range(length))
    return secret_key

# Generate a random secret key of length 4
secret_key = generate_secret_key()
print(secret_key)
