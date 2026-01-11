import bcrypt
from zxcvbn import zxcvbn


def is_common_password(password: str) -> bool:
    with open("common_passwords.txt", "r", encoding="utf-8") as f:
        common_passwords = {line.strip().lower() for line in f if line.strip()}
    return password.lower() in common_passwords


def check_strength(password: str) -> dict:
    analysis = zxcvbn(password)
    return {
        "score": analysis["score"],  # 0-4
        "crack_time": analysis["crack_times_display"]["offline_fast_hashing_1e10_per_second"],
        "feedback": analysis["feedback"]["suggestions"],
    }


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)


def verify_password(password: str, stored_hash: bytes) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), stored_hash)


def main() -> None:
    password = input("Enter a password: ")

    if is_common_password(password):
        print("This password is too common. Pick a less common password.")
        return

    strength = check_strength(password)
    print(f"\nPassword strength score: {strength['score']} / 4")
    print(f"Estimated crack time: {strength['crack_time']}")

    if strength["feedback"]:
        print("\nSuggestions:")
        for s in strength["feedback"]:
            print(f"- {s}")

    hashed = hash_password(password)
    print("\n Hashed password (bcrypt):")
    print(hashed.decode("utf-8"))

    print("\nVerifying password...")
    print("Verified!" if verify_password(password, hashed) else "Verification failed.")


if __name__ == "__main__":
    main()
