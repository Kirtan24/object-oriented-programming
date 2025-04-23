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

    remote = RemoteControl()

    remote.press_button(light_on)  # Light is ON
    remote.press_button(light_off)  # Light is OFF

    remote.undo()  # Undoing last command... Light is ON
    remote.undo()  # Undoing last command... Light is OFF

if __name__ == "__main__":
    main()