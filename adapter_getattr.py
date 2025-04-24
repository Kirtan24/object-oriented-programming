class Example:
    def __init__(self, value):
        self.value = value

    def __getattr__(self, name):
        print("__getattr__() invoked...")
        return f"'{name}' attribute not found!"

obj = Example(10)

print(obj.value)
print(obj.some_attr)
