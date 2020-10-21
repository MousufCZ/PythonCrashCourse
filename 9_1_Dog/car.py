class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 50

    def get_desc_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        
        """ Set the odometer reading to the given value. Reject
        the change if it attempts to roll the odometer back.
        """

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def reset_odometer(self):
        self.odometer_reading = 0


my_car = Car('audi', 'a4', 2016)
print(my_car.get_desc_name())

#my_car.odometer_reading = 700000
my_car.update_odometer(4300023)
my_car.read_odometer()

print("======================================\n\n")

my_used_car = Car('Merc', 'Zelda', 2016)
print(my_used_car.get_desc_name())

my_used_car.update_odometer(76000)
my_used_car.read_odometer()

print("======================================\n\n")
print("We went to Worthing and back, that is 120 miles.")

my_used_car.increment_odometer(120)
my_used_car.read_odometer()


print("We are reseting the odometer of my existing car.")
my_car.reset_odometer()
my_car.read_odometer()
