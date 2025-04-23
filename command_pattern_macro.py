from abc import ABC, abstractmethod
import queue

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

class StartUp:
    def start(self):
        print("Starting up...")

    def shutdown(self):
        print("Shutting down...")

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

class StartUpCommand(Command):
    def __init__(self, startup):
        self.startup = startup

    def execute(self):
        self.startup.start()

    def undo(self):
        print("Shutting down...")

class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in reversed(self.commands):
            command.undo()


class RemoteControl:
    def press_button(self, command):
        command.execute()

def main():
    light = Light()
    startUp  = StartUp()
    remote = RemoteControl()

    light_on = LightOnCommand(light)
    start_up = StartUpCommand(startUp)

    macro = MacroCommand([light_on, start_up])

    remote.press_button(macro)

    macro.undo()

if __name__ == "__main__":
    main()