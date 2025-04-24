import asyncio
from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    async def update(self, product_name):
        pass

# Concrete Observer
class UserSubscriber(Observer):
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    async def update(self, product_name):
        # Simulating delay
        await asyncio.sleep(1)
        print(f"Notification sent to {self.name} ({self.contact}): '{product_name}' is now in stock.")

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

    async def notify_subscribers(self):
        await asyncio.gather(*(user.update(self.name) for user in self.subscribers))
        self.subscribers.clear()

    async def add_stock(self, quantity):
        was_out_of_stock = self.stock == 0
        self.stock += quantity
        if was_out_of_stock and self.stock > 0:
            await self.notify_subscribers()

    def buy(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
        else:
            print(f"Not enough stock for '{self.name}'.")

async def main():
    iPhone = Product("iPhone 15 Pro Max")

    # Subscribers
    user1 = UserSubscriber("Alice", "alice@example.com")
    user2 = UserSubscriber("Bob", "+919999999999")
    iPhone.subscribe(user1)
    iPhone.subscribe(user2)

    await iPhone.add_stock(10)

    iPhone.buy(10)

    user3 = UserSubscriber("Charlie", "charlie@example.com")
    iPhone.subscribe(user3)

    await iPhone.add_stock(5)

asyncio.run(main())
