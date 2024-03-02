class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class OffRoadVehicle(Vehicle):
    def __init__(self, brand, model, year, four_wheel_drive):
        super().__init__(brand, model, year)
        self.four_wheel_drive = four_wheel_drive

class SportsCar(Vehicle):
    def __init__(self, brand, model, year, max_speed):
        super().__init__(brand, model, year)
        self.max_speed = max_speed

# Create instances of each class
vehicle = Vehicle("Toyota", "Corolla", 2022)
off_road_vehicle = OffRoadVehicle("Jeep", "Wrangler", 2023, True)
sports_car = SportsCar("Ferrari", "458 Italia", 2024, 320)

# Display properties of each instance
print("Vehicle:")
print("Brand:", vehicle.brand)
print("Model:", vehicle.model)
print("Year:", vehicle.year)

print("\nOff-Road Vehicle:")
print("Brand:", off_road_vehicle.brand)
print("Model:", off_road_vehicle.model)
print("Year:", off_road_vehicle.year)
print("Four-Wheel Drive:", "Yes" if off_road_vehicle.four_wheel_drive else "No")

print("\nSports Car:")
print("Brand:", sports_car.brand)
print("Model:", sports_car.model)
print("Year:", sports_car.year)
print("Max Speed:", sports_car.max_speed, "km/h")