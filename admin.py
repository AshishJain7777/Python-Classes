class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name  = last_name
        self.login_attempts = 0
        # self.privileges = Admin()
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

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []
    def show_privileges(self):
        for i in self.privileges:
            print('-'+ i)
        

login = ['admin']
main = input('Please Enter The Username: ')
if  main == login[0] :
    my_name = Admin('Ashish','Jain')
    my_name.describrs_user()
    my_name.greet_user()
    my_name.privileges = ['Can Add Post','Can Delete Post','Can Ban User']
    my_name.show_privileges()
else:
    print('No Access')