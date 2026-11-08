from user import User

user = User("Budi", "Santoso", 20, "Boyolali", "budi@example.com")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Percobaan login: {user.login_attempts}")

user.reset_login_attempts()
print(f"Percobaan login setelah reset: {user.login_attempts}")