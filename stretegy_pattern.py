from abc import ABC, abstractmethod

# Abstract Strategy
class MovementStrategy(ABC):
    @abstractmethod
    def move(self):
        pass

# Concrete Strategies
class WalkStrategy(MovementStrategy):
    def move(self):
        return "Walking"

class SwimStrategy(MovementStrategy):
    def move(self):
        return "Swimming"

class FlyStrategy(MovementStrategy):
    def move(self):
        return "Flying"

# Context class
class Animal:
    def __init__(self, name, movement_strategy=None):
        self.name = name
        self.movement_strategy = movement_strategy

    def perform_move(self):
        if self.movement_strategy:
            print(f"{self.name} is {self.movement_strategy.move()}.")
        else:
            print(f"{self.name} doesn't know how to move.")

    def change_movement_strategy(self, movement_strategy):
        self.movement_strategy = movement_strategy

def main():
    duck = Animal("Duck", FlyStrategy())
    fish = Animal("Fish", SwimStrategy())
    turtle = Animal("Turtle", WalkStrategy())

    duck.perform_move()
    fish.perform_move()
    turtle.perform_move()

    duck.change_movement_strategy(SwimStrategy())
    duck.perform_move()

if __name__ == "__main__":
    main()
