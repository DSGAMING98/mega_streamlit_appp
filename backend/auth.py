import os
import json
import hashlib

AUTH_FILE = "data/users.json"

def ensure_auth_file():
    if not os.path.exists(AUTH_FILE):
        with open(AUTH_FILE, "w") as f:
            json.dump({}, f)

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username: str, password: str) -> bool:
    ensure_auth_file()
    with open(AUTH_FILE, "r") as f:
        users = json.load(f)

    if username in users:
        return False

    users[username] = hash_password(password)
    with open(AUTH_FILE, "w") as f:
        json.dump(users, f)
    return True

def authenticate_user(username: str, password: str) -> bool:
    ensure_auth_file()
    with open(AUTH_FILE, "r") as f:
        users = json.load(f)

    return users.get(username) == hash_password(password)
def authenticate_user(username: str, password: str) -> bool:
    ensure_auth_file()
    with open(AUTH_FILE, "r") as f:
        users = json.load(f)

    hashed_input = hash_password(password)
    stored_hash = users.get(username)

    # Debug prints
    print("Trying login for:", username)
    print("Entered password hash:", hashed_input)
    print("Stored hash:", stored_hash)

    return stored_hash == hashed_input
