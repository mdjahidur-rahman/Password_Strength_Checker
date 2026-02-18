import re
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

password = input("Enter a password to check its strength: ")

# Regex patterns
length_pattern = r'.{8,}'            # At least 8 characters
upper_pattern = r'[A-Z]'             # At least one uppercase
lower_pattern = r'[a-z]'             # At least one lowercase
digit_pattern = r'\d'                 # At least one number
special_pattern = r'[^A-Za-z0-9]'    # At least one special character

# Check patterns
length_ok = bool(re.search(length_pattern, password))
has_upper = bool(re.search(upper_pattern, password))
has_lower = bool(re.search(lower_pattern, password))
has_digit = bool(re.search(digit_pattern, password))
has_special = bool(re.search(special_pattern, password))

# Missing rules
missing = []
if not length_ok: missing.append("at least 8 characters")
if not has_upper: missing.append("an uppercase letter")
if not has_lower: missing.append("a lowercase letter")
if not has_digit: missing.append("a number")
if not has_special: missing.append("a special character")

# Score
score = sum([has_upper, has_lower, has_digit, has_special])
if len(password) >= 12:  # bonus for long passwords
    score += 1

# Strength with color
if score <= 2:
    strength = f"{Fore.RED}Weak 🔴{Style.RESET_ALL}"
elif score == 3:
    strength = f"{Fore.YELLOW}Moderate 🟠{Style.RESET_ALL}"
elif score == 4:
    strength = f"{Fore.GREEN}Strong 🟢{Style.RESET_ALL}"
else:
    strength = f"{Fore.MAGENTA}Very Strong 🟣{Style.RESET_ALL}"

# Print results
print("\nPassword strength:", strength)
if missing:
    print(Fore.CYAN + "To improve your password, add: " + ", ".join(missing))
else:
    print(Fore.CYAN + "Your password meets all basic strength requirements!")
