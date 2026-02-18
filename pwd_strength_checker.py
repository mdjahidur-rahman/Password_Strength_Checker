# Step 1: Get user input
password = input("Enter a password to check its strength: ")

# Check length first
length_ok = len(password) >= 8



 # Initialize checks
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)  # not letter or number

# Initialize missing rules list
missing = []

if not length_ok:
    missing.append("at least 8 characters")
if not has_upper:
    missing.append("an uppercase letter")
if not has_lower:
    missing.append("a lowercase letter")
if not has_digit:
    missing.append("a number")
if not has_special:
    missing.append("a special character")

# Calculate strength score
score = 0
if has_upper: score += 1
if has_lower: score += 1
if has_digit: score += 1
if has_special: score += 1
if len(password) >= 12:  # bonus point for long passwords
    score += 1

# Give strength rating
if score <= 2:
    strength = "Weak 🔴"
elif score == 3:
    strength = "Moderate 🟠"
elif score == 4:
    strength = "Strong 🟢"
else:  # score 5
    strength = "Very Strong 🟣"

print("Password strength:", strength)

if missing:
    print("To improve your password, add:", ", ".join(missing))
else:
    print("Your password meets all basic strength requirements!")



