class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def meow(self):
        return "Meow!"

class Bird:
    def tweet(self):
        return "Tweet tweet!"

# Generic Adapter using __getattr__ (no ABC involved)
class GenericAdapter:
    def __init__(self, adaptee, method_mapping):
        self.adaptee = adaptee
        self.method_mapping = method_mapping

    def __getattr__(self, name):
        if name in self.method_mapping:
            actual_method = self.method_mapping[name]
            return getattr(self.adaptee, actual_method)
        raise AttributeError(f"'{type(self.adaptee).__name__}' object has no attribute '{name}'")

# Client code expecting 'make_sound()'
def animal_sound(animal):
    print(animal.make_sound())

# Objects
dog = Dog()
cat = Cat()
bird = Bird()

# No adapter needed for Dog
animal_sound(dog)

# Use __getattr__ adapter for Cat and Bird
cat_adapter = GenericAdapter(cat, {'make_sound': 'meow'})
bird_adapter = GenericAdapter(bird, {'make_sound': 'tweet'})

animal_sound(cat_adapter)   # Output: Meow!
animal_sound(bird_adapter)  # Output: Tweet tweet!