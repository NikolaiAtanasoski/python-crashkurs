from car import Car

new_car = Car("BMW", "m4", "2021")
print(new_car.get_descriptive_name())

new_car.odometer_reading = 23
new_car.read_odometer()