class Registrar:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.participants = {}
        return cls._instance

    def register(self, name, event):
        self.participants[name] = event
        print(f"{name} has been registered for {event}")

    def get_participants(self):
        return self.participants

registrar1 = Registrar()
registrar1.register("John", "Python Workshop")
registrar1.register("Doe", "Cultural Event")
print(registrar1.get_participants())
registrar2 = Registrar()
registrar2.register("Jane", "Concert")
print(registrar1.get_participants())    
print(registrar2.get_participants())