from user import User


class Admin(User):
    """Administrator, jenis khusus dari pengguna."""

    def __init__(self, first_name, last_name, age, city, email):
        super().__init__(first_name, last_name, age, city, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Hak akses administrator:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin("Rina", "Wijaya", 30, "Solo", "rina@example.com")
admin.describe_user()
admin.show_privileges()