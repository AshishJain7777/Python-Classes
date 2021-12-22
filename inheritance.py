class PetrolCar:
    """A Simple Attempt To Represent A Car """
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model} "
        return long_name.title()
    def read_odometer(self):
        print(f"The Car Has {self.odometer_reading} Miles On It.")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You Can't Roll Back An Odometer! ")
    def increment_odometer(self,miles):
        self.odometer_reading += miles
    def fill_gas_tank(self):
        print("O.k. Filled")
####################################################
class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f'This Car Has A {self.battery_size}- KWh Battery')
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f'This Car Can Go About {range} Miles In A Single Charge')
####################################################
class ElectricCar(PetrolCar):
    """ Represent Aspect Of A Car, Specific To Electric Vehicles"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()        
    def fill_gas_tank(self):
        print("This Car Doesn't Need Gas")



my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
my_tesla.battery.get_range()

my_honda = PetrolCar('Honda','civic',2018)
print(my_honda.get_descriptive_name())
my_honda.fill_gas_tank()


