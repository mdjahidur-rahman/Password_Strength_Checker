from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

password = input("Enter a password to check its strength: ")

# Check length
length_ok = len(password) >= 8

# Character type checks
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

# Missing rules
missing = []
if not length_ok: missing.append("at least 8 characters")
if not has_upper: missing.append("an uppercase letter")
if not has_lower: missing.append("a lowercase letter")
if not has_digit: missing.append("a number")
if not has_special: missing.append("a special character")

# Score
score = 0
if has_upper: score += 1
if has_lower: score += 1
if has_digit: score += 1
if has_special: score += 1
if len(password) >= 12: score += 1

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
