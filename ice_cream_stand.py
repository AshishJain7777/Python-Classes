class Restraunt:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_served = 0
        self.ice_creams = Ice_cream_stand()
    def restraunt_name(self):
        print(f'The Name Of The Restraunt Is {self.name.title()}. ')
    def restraunt_type(self):
        print(f'The Cuisine Type Is {self.type.title()}.')
    def people_served(self):
        print(f'People Served In Here Are {self.number_served}.')
    def increament_people(self,people):
        if people >= self.number_served:
            self.number_served = people
        else:
            print('It Is Invalid Value To Increase')    

class Ice_cream_stand:
    def ice_cream_counter(self):
        count = 0
        ice_creams = ['vanilla','chocolate',"Cookies 'N' Cream" , 'mint chocolate chip' , 'buttered pecan', 'cookie dough']
        print('Types Of The Ice Cream We Have Here Are:- ')
        for i in ice_creams:
            count += 1
            print(count,i.title())

my_hotel = Restraunt('Jains','american')
my_hotel.restraunt_name()
my_hotel.restraunt_type()
my_hotel.increament_people(25)
my_hotel.people_served()
my_hotel.ice_creams.ice_cream_counter()