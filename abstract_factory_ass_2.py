from abc import ABC, abstractmethod

# Create Abstract Classes
class ElectricVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class PetrolVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Create Concrete Classes
class ElectricCar(ElectricVehicle):
    def start_engine(self):
        print("Electric car started")

class ElectricBike(ElectricVehicle):
    def start_engine(self):
        print("Electric bike started")

class PetrolCar(PetrolVehicle):
    def start_engine(self):
        print("Petrol car started")

class PerolBike(PetrolVehicle):
    def start_engine(self):
        print("Petrol bike started")

# Create Abstract Factory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_bike(self):
        pass

# Create Concrete Factories
class ElectricVehicleFactory:
    def create_car(self) -> ElectricCar:
        return ElectricCar()

    def create_bike(self) -> ElectricBike:
        return ElectricBike()

class PetrolVehicleFactory:
    def create_car(self) -> PetrolCar:
        return PetrolCar()

    def create_bike(self) -> PerolBike:
        return PerolBike()

# Main Function
def main():
    electric_vehicle_factory = ElectricVehicleFactory()
    petrol_vehicle_factory = PetrolVehicleFactory()

    electric_car = electric_vehicle_factory.create_car()
    electric_car.start_engine()

    petrol_car = petrol_vehicle_factory.create_car()
    petrol_car.start_engine()

    electric_bike = electric_vehicle_factory.create_bike()
    electric_bike.start_engine()

    petrol_bike = petrol_vehicle_factory.create_bike()
    petrol_bike.start_engine()

if __name__ == "__main__":
    main()