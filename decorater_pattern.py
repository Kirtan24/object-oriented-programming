from abc import ABC, abstractmethod

# Base Interface
class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        pass
    def get_cost(self):
        pass

# Concrete Classes
class Margerita(Pizza):
    def get_description(self):
        return "Margerita Pizza"
    def get_cost(self):
        return 100

class Farmhouse(Pizza):
    def get_description(self):
        return "Farmhouse Pizza"
    def get_cost(self):
        return 150

# Concreet Abstract Decorator
class PizzaDecorater(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza
    def get_description(self):
        return self.pizza.get_description()
    def get_cost(self):
        return self.pizza.get_cost()

# Concrete Decorators
class Cheese(PizzaDecorater):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
    def get_description(self):
        return super().get_description() + ", Extra Cheese"
    def get_cost(self):
        return super().get_cost() + 10

class Tomato(PizzaDecorater):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
    def get_description(self):
        return super().get_description() + ", Added Tomato"
    def get_cost(self):
        return super().get_cost() + 15

class Olive(PizzaDecorater):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
    def get_description(self):
        return super().get_description() + ", Added Olive"
    def get_cost(self):
        return super().get_cost() + 20

class Jalapeno(PizzaDecorater):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
    def get_description(self):
        return super().get_description() + ", Added Jalapeno"
    def get_cost(self):
        return super().get_cost() + 25

# Use the Decorater
def main():
    pizza1 = Margerita()
    print(f"{pizza1.get_description()} costs {pizza1.get_cost()}")

    pizza1 = Cheese(pizza1)
    print(f"{pizza1.get_description()} costs {pizza1.get_cost()}")

    pizza1 = Tomato(pizza1)
    print(f"{pizza1.get_description()} costs {pizza1.get_cost()}")

    pizza1 = Olive(pizza1)
    print(f"{pizza1.get_description()} costs {pizza1.get_cost()}")

    pizza1 = Jalapeno(pizza1)
    print(f"{pizza1.get_description()} costs {pizza1.get_cost()}")


    # pizza2 = Farmhouse()
    # print(f"{pizza2.get_description()} costs {pizza2.get_cost()}")

    # pizza2 = Tomato(Olive(Cheese(pizza2)))
    # print(f"{pizza2.get_description()} costs {pizza2.get_cost()}")

    # Alternate way to create pizza
    pizza2 = Tomato(Olive(Cheese(Farmhouse())))
    print(f"{pizza2.get_description()} costs {pizza2.get_cost()}")


if __name__ == "__main__":
    main()