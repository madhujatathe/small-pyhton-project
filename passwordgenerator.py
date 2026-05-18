import random
import string


def generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True):
    characters = ""

    if use_letters:
        characters += string.ascii_letters  # a-z A-Z

    if use_digits:
        characters += string.digits  # 0-9

    if use_symbols:
        characters += string.punctuation  # !@#$%^&*()...

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    letters = input("Include letters? (y/n): ").lower() == "y"
    digits = input("Include digits? (y/n): ").lower() == "y"
    symbols = input("Include symbols? (y/n): ").lower() == "y"

    try:
        password = generate_password(length, letters, digits, symbols)
        print("\nGenerated Password:")
        print(password)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
