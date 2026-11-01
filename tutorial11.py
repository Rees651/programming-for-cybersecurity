class User:
    def __init__(self, username):
        self.username = username

    def display(self):
        print("User:", self.username)


class Admin(User):
    pass


class Guest(User):
    pass


admin1 = Admin("Lilly")
guest1 = Guest("Chris")

admin1.display()
guest1.display()
