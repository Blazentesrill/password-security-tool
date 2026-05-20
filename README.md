# password-security-tool

A Python command-line tool that checks password strength, screens against common passwords, hashes using bcrypt, and verifies the result. Built to demonstrate secure authentication practices as part of CS 4683 (Secure Software Development and Analysis) at UTSA.

---

## Features

- **Common password check** — screens input against a list of frequently used passwords before doing anything else
- **Strength estimation** — uses [zxcvbn](https://github.com/dwolfhub/zxcvbn-python), a realistic password strength estimator that accounts for patterns, dictionary words, and keyboard walks rather than just character counts
- **Secure hashing** — hashes passwords with [bcrypt](https://pypi.org/project/bcrypt/), including automatic salt generation
- **Verification** — confirms a plaintext password matches a stored bcrypt hash

---

## Why these tools?

**bcrypt over MD5/SHA-256:** General-purpose hash functions like MD5 and SHA-256 are designed to be fast, which makes them poor choices for passwords — an attacker can test billions of guesses per second against a leaked hash. bcrypt is intentionally slow and includes a cost factor, making brute-force attacks significantly more expensive.

**zxcvbn over character rules:** Rule-based checkers ("must have a number and a symbol") are easy to game with passwords like `Password1!` that are still weak. zxcvbn estimates actual crack time by matching against real-world password patterns, dictionary words, and common substitutions.

---

## Installation

```bash
pip install bcrypt zxcvbn
```

---

## Usage

```bash
python password_checker.py
```

Example output:

```
Enter a password: correct-horse-battery

Password strength score: 4 / 4
Estimated crack time: centuries

Hashed password (bcrypt):
$2b$12$e0NnJbBMkFEKyMtBdS5AReXaXqJBMJ9v6xW1Kz3v2yHqLmP8OdTWu

Verifying password...
Verified!
```

---

## Common Passwords List

`common_passwords.txt` ships with a small sample list for demonstration. For real-world use, drop in a larger list such as the [SecLists Top 1000](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt) — the tool will work with any newline-separated `.txt` file.

---

## Project Structure

```
password-security-tool/
├── password_checker.py     # Main script
├── common_passwords.txt    # Sample blocklist
└── README.md
```

---

## Disclaimer

This tool is a demo. It demonstrates password security concepts and is not production hardened (e.g. no CLI argument handling, no logging, no rate limiting).
