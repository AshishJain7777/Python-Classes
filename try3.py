class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name  = last_name
        self.login_attempts = 0
    def describrs_user(self):
        print(f'First Name: {self.first_name} \nLast Name: {self.last_name}')
    def greet_user(self):
        print(f'Welcome! {self.first_name}')
    def increament_login_attempts(self):
        self.login_attempts += 1
        print(f'Login Attempts = {self.login_attempts}')
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Reset To Initaial Value Login Attempts = {self.login_attempts}')

    
my_name = User('Ashish','Jain')
my_name.describrs_user()
my_name.greet_user()
my_name.increament_login_attempts()
my_name.increament_login_attempts()
my_name.increament_login_attempts()
my_name.reset_login_attempts()