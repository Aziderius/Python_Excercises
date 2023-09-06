class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(type(School_bus))
print("Is the School Bus an instance of the Vehicle Class?", isinstance(School_bus, Vehicle))

if isinstance(School_bus, Vehicle) == True:
    print(":D")
else:
    print("D:")