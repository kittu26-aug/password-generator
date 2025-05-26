import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """
    Generates a random password based on specified criteria.

    Args:
        length (int): The desired length of the password. Defaults to 12.
        use_uppercase (bool): Whether to include uppercase letters. Defaults to True.
        use_lowercase (bool): Whether to include lowercase letters. Defaults to True.
        use_digits (bool): Whether to include digits. Defaults to True.
        use_symbols (bool): Whether to include symbols. Defaults to True.

    Returns:
        str: The generated password.
    """
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected for password generation. Please select at least one.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("--- Password Generator ---")

    try:
        # Get desired password length from user
        while True:
            try:
                length_str = input("Enter desired password length (default 12): ")
                length = int(length_str) if length_str else 12
                if length <= 0:
                    print("Password length must be a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number for the length.")

        # Get character type preferences from user
        use_uppercase = input("Include uppercase letters? (y/n, default y): ").lower() in ('y', '')
        use_lowercase = input("Include lowercase letters? (y/n, default y): ").lower() in ('y', '')
        use_digits = input("Include digits? (y/n, default y): ").lower() in ('y', '')
        use_symbols = input("Include symbols? (y/n, default y): ").lower() in ('y', '')

        generated_pwd = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        print(f"\nGenerated Password: {generated_pwd}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")