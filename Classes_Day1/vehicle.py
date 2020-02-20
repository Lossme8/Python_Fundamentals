class Vehicle:
    def general_usage(self):
        print("general use: transportation")


class Car(Vehicle):
    def __init__(self):
        print("\nI'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("\nspecific use: commute to work, vacation with family")


class MotorCycle(Vehicle):
    def __init__(self):
        print("\nI'm motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("\nspecific usage: road trip, racing")


c = Car()
m = MotorCycle()

print(issubclass(Car,Vehicle))
