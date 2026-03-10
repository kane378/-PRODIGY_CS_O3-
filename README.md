# Prodigy InfoTech - Cybersecurity Internship
## Task 03: Password Complexity Checker

This tool analyzes the strength of a password by checking it against several security metrics, including character variety and length.

### 🛡️ Security Criteria
- **Length**: 8+ characters.
- **Uppercase/Lowercase**: Mixture of cases.
- **Numerical**: Presence of digits.
- **Special Characters**: Presence of symbols (e.g., @, #, $).

### 🚀 How to Run
1. Ensure Python is installed.
2. Run the script:
   ```bash
   python password_check.py

### Final Tip: Don't Push Real Passwords!
When you test this, don't use your actual personal passwords. Even though this script stays on your computer, it's good practice in cybersecurity to use "dummy" passwords like `Test@1234` or `Coding_Is_Fun_2026`.

## 🛡️ Pro-Security Recommendations
While this tool checks for complexity, a strong password is only the first line of defense. For complete security, I recommend:

1. **MFA (Multi-Factor Authentication)**: Even if a password is stolen, MFA provides a second layer of protection (e.g., TOTP apps or Hardware Keys).
2. **Password Salting**: In a real application, passwords should be hashed using algorithms like `Argon2` or `bcrypt` with a unique "salt" to prevent rainbow table attacks.
3. **Zero-Trust**: Treat every password as potentially compromised and monitor for unusual login activity.