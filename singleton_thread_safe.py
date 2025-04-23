import threading

class Registrar:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.participants = {}
        return cls._instance

    def register(self, name, event):
        with self._lock:
            self.participants[name] = event
            print(f"{name} has been registered for {event}")

    def get_participants(self):
        return self.participants

def reegister_participant(name, event):
    registrar = Registrar()
    registrar.register(name, event)

thread1 = threading.Thread(target=reegister_participant, args=("John", "Python Workshop"))
thread2 = threading.Thread(target=reegister_participant, args=("Doe", "Culture Event"))
thread3 = threading.Thread(target=reegister_participant, args=("Jane", "Concert"))

thread1.start()
thread1.join()
print(Registrar().get_participants())

thread2.start()
thread2.join()
print(Registrar().get_participants())

thread3.start()
thread3.join()
print(Registrar().get_participants())