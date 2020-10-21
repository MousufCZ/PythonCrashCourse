from car import Car
from my_electric_car import ElectricCar
from my_electric_car import Battery

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())


my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.battery_size = 80
print(my_tesla.battery.describe_battery())
print(my_tesla.battery.get_range())
