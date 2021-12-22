class Restraunt:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_served = 0
    def restraunt_name(self):
        print(f'The Name Of The Restraunt Is {self.name}. ')
    def restraunt_type(self):
        print(f'The Cuisine Type Is {self.type}.')
    def people_served(self):
        print(f'People Served In Here Are {self.number_served}.')
    def increament_people(self,people):
        if people >= self.number_served:
            self.number_served = people
        else:
            print('It Is Invalid Value To Increase')    

my_place = Restraunt('Manvik','Continental')
my_place.restraunt_name()
my_place.restraunt_type()
my_place.people_served()
my_place.increament_people(5)
my_place.people_served()