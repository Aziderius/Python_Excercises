class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f"Vehicle name: \n{self.name} \n{self.max_speed} mph \nMilage: {self.mileage}"

class School_Volvo_Speed(Vehicle):
    pass

bus = School_Volvo_Speed("School Volvo Speed", 180, 12)
print(bus)