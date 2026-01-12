import random
import string

# ---------------- PASSWORD STRENGTH CHECKER ----------------
def check_password_strength(password):
    upper_case = lower_case = digit = special_char = False
    special_characters = "!@#$%^&*()-+?_=,<>/"
    for char in password:
        if char.isupper():
            upper_case = True
        elif char.islower():
            lower_case = True
        elif char.isdigit():
            digit = True
        elif char in special_characters:
            special_char = True
    length_valid = len(password) >= 8
    score = sum([upper_case, lower_case, digit, special_char, length_valid])
    if score <= 2:
        return "VERY WEAK PASSWORD"
    elif score == 3:
        return "MEDIUM STRENGTH PASSWORD"
    else:
        return "STRONG PASSWORD"


# ---------------- PASSWORD GENERATOR ----------------
def generate_strong_password(include_initials, initials=""):
    length = 8
    if include_initials.lower() == "yes" and initials:
        length -= len(initials)
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-+?_=,<>/"
    password = ""
    for _ in range(length):
        password += random.choice(all_chars)
    if include_initials.lower() == "yes" and initials:
        password += initials
    return password


# ---------------- MENU ----------------
def menu():
    while True:
        print("\n1. CHECK PASSWORD STRENGTH")
        print("2. GENERATE STRONG PASSWORD")
        print("3. EXIT")
        choice = input("Enter your choice (1-3): ")
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue
        choice = int(choice)
        if choice == 1:
            password = input("Enter your password: ")
            result = check_password_strength(password)
            print("Your password strength is:", result)
        elif choice == 2:
            recommend = input("Do you want to add initials? (yes/no): ")
            initials = ""
            if recommend.lower() == "yes":
                initials = input("Enter initials: ")
            pwd = generate_strong_password(recommend, initials)
            print("Your strong password is:", pwd)
        elif choice == 3:
            print("Exiting program. Stay secure 🔐")
            break
        else:
            print("Invalid choice.")

menu()
