from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Light:
    def turn_on(self):
        print("The light is on")

    def turn_off(self):
        print("The light is off")

class TurnOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class TurnOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

# 클라이언트 코드
light = Light()
turn_on_command = TurnOnCommand(light)
remote = RemoteControl()

remote.set_command(turn_on_command)
remote.press_button()

turn_off_command = TurnOffCommand(light)
remote.set_command(turn_off_command)
remote.press_button()