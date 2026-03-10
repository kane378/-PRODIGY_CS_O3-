import re

def check_password_strength(password):
    # Assessment criteria
    score = 0
    feedback = []

    # 1. Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• Make it at least 8 characters long.")

    # 2. Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("• Add at least one uppercase letter (A-Z).")

    # 3. Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("• Add at least one lowercase letter (a-z).")

    # 4. Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("• Include at least one number (0-9).")

    # 5. Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("• Use a special character (e.g., !, @, #, $).")

    # Final Strength Rating
    ratings = {
        0: "Very Weak 🔴",
        1: "Very Weak 🔴",
        2: "Weak 🟠",
        3: "Moderate 🟡",
        4: "Strong 🟢",
        5: "Excellent 💎"
    }

    return ratings[score], feedback

# --- Simple User Interface ---
print("--- Password Security Auditor ---")
user_pwd = input("Enter a password to test: ")

strength, suggestions = check_password_strength(user_pwd)

print(f"\nStrength Rating: {strength}")

if suggestions:
    print("How to improve:")
    for tip in suggestions:
        print(tip)
else:
    print("Great job! This is a secure password.")
def get_security_advice():
    print("\n🛡️  Beyond the Password: Professional Recommendations")
    print("-" * 50)
    print("1. Enable MFA/2FA: Always use Multi-Factor Authentication where possible.")
    print("2. Use a Manager: Don't reuse passwords; use a Password Manager (e.g., Bitwarden).")
    print("3. Hashing & Salting: If you were storing this in a database, never store it as plain text.")
    print("4. Avoid Personal Info: Don't include your name, birthday, or 'VNRVJIET' in the string.")