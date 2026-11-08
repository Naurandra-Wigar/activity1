from pathlib import Path
import json

path = Path(__file__).parent / "username.json"


def get_stored_username(path):
    """Ambil nama yang tersimpan, kalau ada."""
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    return None


def get_new_username(path):
    """Minta nama baru dan simpan."""
    username = input("Siapa namamu? ")
    path.write_text(json.dumps(username))
    return username


def greet_user():
    """Sapa pengguna dengan namanya, setelah memastikan orangnya benar."""
    username = get_stored_username(path)
    if username:
        correct = input(f"Apakah kamu {username}? (y/n) ")
        if correct == "y":
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username(path)
            print(f"Kami akan mengingatmu, {username}!")
    else:
        username = get_new_username(path)
        print(f"Kami akan mengingatmu, {username}!")


greet_user()