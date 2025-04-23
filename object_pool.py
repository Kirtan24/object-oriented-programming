import time
import queue

class Car:
    """Represents a Car object with a unique ID."""
    def __init__(self, car_id):
        self.car_id = car_id

    def __str__(self):
        return f"Car-{self.car_id}"

class CarPool:
    """Manages a pool of reusable Car objects."""
    def __init__(self, total_cars):
        self.available_cars = queue.Queue()
        self.in_use_cars = set()

        # Pre-create car objects and add them to the queue
        for car_id in range(1, total_cars + 1):
            self.available_cars.put(Car(car_id))

    def rent_car(self):
        """Rent a car if available; else notify customer."""
        if not self.available_cars.empty():
            car = self.available_cars.get()
            self.in_use_cars.add(car)
            print(f"Car {car} has been rented out.")
            return car
        else:
            print("No cars available! Please wait.")
            return None

    def return_car(self, car):
        """Return a rented car to the pool for reuse."""
        if car in self.in_use_cars:
            self.in_use_cars.remove(car)
            self.available_cars.put(car)
            print(f"Car {car} has been returned and is available for rent.")
        else:
            print("Error: This car does not belong to the rental service!")

# Simulating the car rental process
if __name__ == "__main__":
    car_pool = CarPool(total_cars=3)  # Creating a pool of 3 cars

    # Customers renting cars
    car1 = car_pool.rent_car()
    car2 = car_pool.rent_car()
    car3 = car_pool.rent_car()
    car4 = car_pool.rent_car()  # No cars available!

    time.sleep(1)  # Simulate some delay

    # Customers returning cars
    if car1:
        car_pool.return_car(car1)

    time.sleep(1)  # Simulate some delay

    # Another customer rents a car after one is returned
    car5 = car_pool.rent_car()
