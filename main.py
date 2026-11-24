
import secrets
import string
import math


def generate_password(length=16, use_symbols=True):
    characters = string.ascii_letters + string.digits

    if use_symbols:
        characters += string.punctuation

    password = ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password



def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Medium"

    return "Strong"


def calculate_entropy(password):
    pool_size = 0

    if any(c.islower() for c in password):
        pool_size += 26

    if any(c.isupper() for c in password):
        pool_size += 26

    if any(c.isdigit() for c in password):
        pool_size += 10

    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    if pool_size == 0:
        return 0

    return len(password) * math.log2(pool_size)


def main():
    print("=" * 40)
    print("       PASSWORD GENERATOR")
    print("=" * 40)

    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            return

        symbols = input("Include symbols? (y/n): ").lower() == "y"

        password = generate_password(length, symbols)

        print("\nGenerated Password:")
        print(password)

        strength = check_strength(password)
        entropy = calculate_entropy(password)

        print("\nPassword Analysis")
        print("-" * 30)
        print(f"Length: {length}")
        print(f"Strength: {strength}")
        print(f"Estimated entropy: {entropy:.2f} bits")
        print("-" * 30)

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
