import queue
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class Light:
    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

class RemoteControl:
    def __init__(self):
        self.history = []

    def press_button(self, command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            last_command = self.history.pop()
            print("Undoing last command...")
            last_command.undo()

def main():
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    task_queue = queue.Queue()
    task_queue.put(light_on)
    task_queue.put(light_off)
    task_queue.put(light_on)

    print("Executing commands from the queue:")
    while not task_queue.empty():
        command = task_queue.get()
        command.execute()

if __name__ == "__main__":
    main()