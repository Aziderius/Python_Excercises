class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f"The Vehicle have a max speed of {self.max_speed} mph and have {self.mileage} mileage"

corvette = Vehicle(195, 10_000)

print(corvette)