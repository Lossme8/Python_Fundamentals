from car import Car, ElectricCar

my_new_car = Car('bmw', '325', 1970)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', '2016')
print(my_tesla.get_descriptive_name())
