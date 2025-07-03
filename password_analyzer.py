import math
import random
import string

# Character sets
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = string.punctuation

def calculate_entropy(password):
    pool = 0
    if any(c in LOWER for c in password): pool += len(LOWER)
    if any(c in UPPER for c in password): pool += len(UPPER)
    if any(c in DIGITS for c in password): pool += len(DIGITS)
    if any(c in SYMBOLS for c in password): pool += len(SYMBOLS)
    if pool == 0: return 0
    return round(len(password) * math.log2(pool), 2)

def estimate_crack_time(entropy):
    guesses = 2 ** entropy
    seconds = guesses / 1e9
    if seconds < 60:
        return f"{int(seconds)} seconds"
    elif seconds < 3600:
        return f"{int(seconds / 60)} minutes"
    elif seconds < 86400:
        return f"{int(seconds / 3600)} hours"
    elif seconds < 31536000:
        return f"{int(seconds / 86400)} days"
    else:
        return f"{int(seconds / 31536000)} years"

def generate_strong_password(length=16):
    chars = LOWER + UPPER + DIGITS + SYMBOLS
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

def analyze_password(password):
    entropy = calculate_entropy(password)
    weaknesses = []
    if len(password) < 12:
        weaknesses.append("Too short")
    if password.lower() in ["password", "123456", "qwerty"]:
        weaknesses.append("Common password")
    if password.isdigit() or password.isalpha():
        weaknesses.append("Lacks character variety")
    if entropy < 60:
        weaknesses.append("Low entropy")
    return {
        "password": password,
        "entropy": entropy,
        "crack_time": estimate_crack_time(entropy),
        "weaknesses": weaknesses,
        "suggestion": generate_strong_password(16)
    }

def analyze_passwords(passwords):
    results = []
    for pwd in passwords:
        results.append(analyze_password(pwd))
    return results

# Example usage
if __name__ == "__main__":
    passwords = ["password123", "P@ssw0rd2025", "7g$L!vQ2#pXz1@w"]
    results = analyze_passwords(passwords)
    for r in results:
        print(f"Password: {r['password']}")
        print(f"  Entropy: {r['entropy']} bits")
        print(f"  Estimated Crack Time: {r['crack_time']}")
        print(f"  Weaknesses: {', '.join(r['weaknesses']) if r['weaknesses'] else 'None'}")
        print(f"  Stronger Suggestion: {r['suggestion']}\n")
