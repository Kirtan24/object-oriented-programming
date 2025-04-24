from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, product_name):
        pass

# Concrete Observer
class UserSubscriber(Observer):
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact  # email or mobile

    def update(self, product_name):
        print(f"Notification: {self.name}, the product '{product_name}' is now in stock. Sent to: {self.contact}")

# Subject (Observable)
class Product:
    def __init__(self, name):
        self.name = name
        self.stock = 0
        self.subscribers = []

    def subscribe(self, user: Observer):
        self.subscribers.append(user)

    def unsubscribe(self, user: Observer):
        if user in self.subscribers:
            self.subscribers.remove(user)

    def notify_subscribers(self):
        for user in self.subscribers:
            user.update(self.name)
        self.subscribers.clear()

    def add_stock(self, quantity):
        was_out_of_stock = self.stock == 0
        self.stock += quantity
        if was_out_of_stock and self.stock > 0:
            self.notify_subscribers()

    def buy(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
        else:
            print(f"Not enough stock for '{self.name}'. Only {self.stock} available.")

# ---------------------
# Usage
# ---------------------
if __name__ == "__main__":
    # Product initially out of stock
    iPhone = Product("iPhone 15 Pro Max")

    # Users subscribe
    user1 = UserSubscriber("Alice", "alice@example.com")
    user2 = UserSubscriber("Bob", "+919999999999")
    iPhone.subscribe(user1)
    iPhone.subscribe(user2)

    # Add stock (should notify both)
    iPhone.add_stock(10)

    # Add more stock (no notification needed)
    iPhone.add_stock(5)

    # Buy all stock
    iPhone.buy(15)

    # New subscriber joins
    user3 = UserSubscriber("Charlie", "charlie@example.com")
    iPhone.subscribe(user3)

    # Refill stock (should notify Charlie)
    iPhone.add_stock(5)