class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

volvo_bus = Bus("School Volvo Speed", 180, 12)
audi_car = Car("Audi Q5", 240, 18)

for vehicles in (volvo_bus, audi_car):
    print (f"Color: {vehicles.color}, Vehicle name: {vehicles.name}, Speed: {vehicles.max_speed} mph, Milage: {vehicles.mileage}")