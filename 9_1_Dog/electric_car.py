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

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def desc_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWH battery")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


    

class ElectricCar(Car):

    """
    Initialize attributes of the parent class.
    Then initialize attributes specific to an electric car.
    """

    def __init__(self, make, model, year):
        #You can override a method from Car class by rewritting the method in child/sub-class
        super().__init__(make, model, year)
        self.battery = Battery()
        
    

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_desc_name())
my_tesla.battery.desc_battery()
my_tesla.battery.get_range()
