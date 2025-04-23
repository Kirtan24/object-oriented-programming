# import random
# import threading
# import time

# class Bike:
#     def __init__(self, size):
#         self.size = size
#         self.in_use = False

#     def rent(self):
#         self.in_use = True
#         print(f"Bike of size {self.size} has been rented")

#     def release(self):
#         self.in_use = False
#         print(f"Bike of size {self.size} has been returned")

# class BikePool:
#     def __init__(self, size=3):
#         self.size = size
#         self.avialable_bikes = [Bike(i+1) for i in range(size)]
#         self.lock = threading.Lock()

#     def aquiare_bike(self):
#         with self.lock:
#             for bike in self.avialable_bikes:
#                 if not bike.in_use:
#                     bike.rent()
#                     return bike
#             print("All bikes are in rented! Please wait.")
#             return None

#     def return_bike(self, bike):
#         with self.lock:
#             if bike in self.avialable_bikes:
#                 bike.release()
#             else:
#                 print("This bike does not belong to this pool")
#                 return None

# def rent_bike(cust_id ,pool):
#     print(f"Customer {cust_id + 1} is trying to rent a bike")
#     bike = pool.aquiare_bike()
#     if bike:
#         time.sleep(random.randint(1, 5))
#         pool.return_bike(bike)

# bike_pool = BikePool()


# threads = []
# for i in range(5):
#     thread = threading.Thread(target=rent_bike, args=(i, bike_pool))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# print("All bikes are returned. Pool is closed now.")


import random
import threading
import time
from queue import Queue

class Bike:
    def __init__(self, size):
        self.size = size
        self.in_use = False

    def rent(self):
        self.in_use = True
        print(f"Bike of size {self.size} has been rented")

    def release(self):
        self.in_use = False
        print(f"Bike of size {self.size} has been returned")

class BikePool:
    def __init__(self, size=3):
        self.size = size
        self.available_bikes = [Bike(i+1) for i in range(size)]
        self.lock = threading.Lock()
        self.waiting_queue = Queue()
        self.active_customers = set()

    def acquire_bike(self, cust_id):
        with self.lock:
            for bike in self.available_bikes:
                if not bike.in_use:
                    bike.rent()
                    self.active_customers.add(cust_id)
                    return bike

            print(f"All bikes are rented! Customer {cust_id + 1} is added to the queue.")
            self.waiting_queue.put(cust_id)
            return None

    def return_bike(self, bike, cust_id):
        with self.lock:
            bike.release()
            self.active_customers.discard(cust_id)
            if not self.waiting_queue.empty():
                next_cust_id = self.waiting_queue.get()
                print(f"Assigning bike of size {bike.size} to waiting Customer {next_cust_id + 1}.")
                threading.Thread(target=rent_bike, args=(next_cust_id, self)).start()


def rent_bike(cust_id, pool):
    print(f"Customer {cust_id + 1} is trying to rent a bike")
    bike = None
    while not bike and cust_id not in pool.active_customers:
        bike = pool.acquire_bike(cust_id)
        if not bike:
            return  # Stop retrying if the request is in the queue
    time.sleep(random.randint(1, 5))
    pool.return_bike(bike, cust_id)

bike_pool = BikePool()

threads = []
num_customers = 5
for i in range(num_customers):
    thread = threading.Thread(target=rent_bike, args=(i, bike_pool))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All bikes are returned. Pool is closed now.")
