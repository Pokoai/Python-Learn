class User():
    def __init__(self, first_name, last_name, city, hobby):
        self.full_name = first_name + last_name
        self.city = city
        self.hobby = hobby
        self.login_attempts = 0


    def describe_user(self):
        # self.full_name = self.first_name + self.last_name
        print(self.full_name.title() + " is in " + self.city.title() + '.')
        print(self.full_name.title() + "'s hobby is " + self.hobby + '.')


    def greet_user(self):
        print(self.full_name.title() + ", welcom to my site!\n")


    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("\n管理员权限:")
        for privilege in self.privileges:
            print(" - " + privilege)


class Admin(User):
    def __init__(self, first_name, last_name, city, hobby):
        super().__init__(first_name, last_name, city, hobby)
        self.privileges = Privileges()


admin = Admin('hu', 'min', 'city', 'programing')
admin.privileges.show_privileges()