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
    

user1 = User('hu', 'min', 'hangzhou', 'program')
user2 = User('zou', 'miao', 'hanghzou', 'sleeping')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3 = User('ruan', 'tang', 'xihu', 'rowing')

for i in range(4):
    user3.increment_login_attempts()
print("Login attempts: " + str(user3.login_attempts) + "\n")

user3.reset_login_attempts()
print("Login attempts: " + str(user3.login_attempts))


