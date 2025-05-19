import random
import string

# Welcome message
print("""
==============================
  Random Password Generator
==============================
""")

def get_password_length():
    """Prompt user for password length and validate input."""
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")

def get_character_sets():
    """Prompt user to select character sets and validate selection."""
    char_sets = []
    print("Select character sets to include in your password:")
    include_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    if include_letters:
        char_sets.append(string.ascii_letters)
    if include_numbers:
        char_sets.append(string.digits)
    if include_symbols:
        char_sets.append(string.punctuation)

    if not char_sets:
        print("You must select at least one character set.")
        return get_character_sets()
    return char_sets

def generate_password(length, char_sets):
    """Generate a random password based on user preferences."""
    all_chars = ''.join(char_sets)
    # Ensure at least one character from each selected set
    password = [random.choice(char_set) for char_set in char_sets]
    # Fill the rest of the password length
    password += [random.choice(all_chars) for _ in range(length - len(password))]
    random.shuffle(password)
    return ''.join(password)

def main():
    length = get_password_length()
    char_sets = get_character_sets()
    password = generate_password(length, char_sets)
    print(f"\nYour generated password is: {password}\n")
    print("Keep it safe and do not share it with others!")

if __name__ == "__main__":
    main() 
