from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    FUEL_CONSUMPTION_INCREASE = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + Car.FUEL_CONSUMPTION_INCREASE)
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    FUEL_CONSUMPTION_INCREASE = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + Truck.FUEL_CONSUMPTION_INCREASE)
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)


# ------------------------------
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
# ------------------------------
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
