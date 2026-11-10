import re
import secrets
import string
import getpass

COMMON_PASSWORDS = {
    "password", "password123", "123456",
    "123456789", "qwerty", "admin",
    "welcome", "iloveyou"
}


def analyze_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Consider using 12 or more characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Include special characters.")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions.append("Avoid commonly used passwords.")

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    print("\n----- PASSWORD ANALYSIS -----")
    print("Password length:", len(password))
    print("Strength:", strength)
    print("Score:", score, "/ 6")

    if suggestions:
        print("\nSuggestions:")
        for item in suggestions:
            print("-", item)
    else:
        print("Great! Your password meets all checks.")

    print("-----------------------------")


def generate_password():
    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*"
    )

    while True:
        password = ''.join(
            secrets.choice(characters) for _ in range(16)
        )

        if (
            re.search(r"[A-Z]", password)
            and re.search(r"[a-z]", password)
            and re.search(r"[0-9]", password)
            and re.search(r"[^A-Za-z0-9]", password)
        ):
            return password


print("================================")
print("     PASSWORD STRENGTH ANALYZER")
print("================================")
print("1. Check Password Strength")
print("2. Generate Strong Password")
print("3. Exit")

choice = input("\nEnter your choice: ")

if choice == "1":
    password = getpass.getpass("Enter password (hidden): ")
    analyze_password(password)

elif choice == "2":
    print("\nGenerated Strong Password:")
    print(generate_password())

elif choice == "3":
    print("Thank you for using the tool!")

else:
    print("Invalid choice. Please try again.")