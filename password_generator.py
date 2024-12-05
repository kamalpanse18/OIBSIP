import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    character_pool = ""

    if use_letters:
        character_pool += string.ascii_letters  # Adds both uppercase and lowercase letters
    if use_numbers:
        character_pool += string.digits         # Adds digits 0-9
    if use_symbols:
        character_pool += string.punctuation    # Adds symbols (!, @, #, etc.)

    if not character_pool:
        print("Error: No character types selected. Please choose at least one character type.")
        return None

    # Generate a password by randomly selecting characters from the pool
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

print("Welcome to the Password Generator!")

# Get password length from user
while True:
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Get character preferences
use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

# Generate and display the password
password = generate_password(length, use_letters, use_numbers, use_symbols)
if password:
    print(f"Generated Password: {password}")