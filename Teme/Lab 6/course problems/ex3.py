# 3 ------------------------------------------------
# Create a base class Vehicle with attributes like make, model, and year, and then
# create subclasses for specific types of vehicles like Car, Motorcycle, and Truck.
# Add methods to calculate mileage or towing capacity based on the vehicle type.

class Vehicle:
    def __init__(self, fuel_capacity, fuel_consum, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_consum = fuel_consum

class Car(Vehicle):
    def __init__(self, fuel_capacity, fuel_consum, make, model, year, horsepower, weight):
        super().__init__(fuel_capacity, fuel_consum, make, model, year)
        self.horsepower = horsepower
        self.weight = weight

    def calc_mileage(self):
        return self.fuel_capacity / self.fuel_consum * 100

    def calc_towing_capacity(self, weight_per_horsepower):
        return self.horsepower * weight_per_horsepower - self.weight

class Motorcycle(Vehicle):
    def __init__(self, fuel_capacity, fuel_consum, make, model, year):
        super().__init__(fuel_capacity, fuel_consum, make, model, year)

    def calc_mileage(self):
        return self.fuel_capacity / self.fuel_consum * 100

class Truck(Vehicle):
    def __init__(self, fuel_capacity, fuel_consum, make, model, year, horsepower, weight):
        super().__init__(fuel_capacity, fuel_consum, make, model, year)
        self.fuel_capacity = fuel_capacity
        self.fuel_consum = fuel_consum
        self.horsepower = horsepower
        self.weight = weight

    def calc_mileage(self):
        return self.fuel_capacity / self.fuel_consum * 100

    def calc_towing_capacity(self, weight_per_horsepower):
        return self.horsepower * weight_per_horsepower - self.weight

car = Car(60, 8, "Audi", "Q6", "2015", 322, 1900)
motorcycle = Motorcycle(30, 5, "Kawasaki", "Ninja ZX-10RR", "2022")
truck = Truck(170, 18, "Mercedes", "Actros L", "2021", 625, 8000)

print("Car mileage:", car.calc_mileage())
print("Car towing cap:", car.calc_towing_capacity(13), "\n")
print("Motorcycle mileage:", motorcycle.calc_mileage(), "\n")
print("Truck mileage:", truck.calc_mileage())
print("Truck towing cap:", truck.calc_towing_capacity(30))