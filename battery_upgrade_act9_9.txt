from user import User


class Privileges:
    """Daftar hak akses untuk administrator."""

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        print("Hak akses administrator:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Administrator, jenis khusus dari pengguna."""

    def __init__(self, first_name, last_name, age, city, email):
        super().__init__(first_name, last_name, age, city, email)
        self.privileges = Privileges()


admin = Admin("Rina", "Wijaya", 30, "Solo", "rina@example.com")
admin.privileges.show_privileges()