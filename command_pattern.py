from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# concrete command
class NoCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class CeilingFanHighCommand(Command):
    def __init__(self, ceilingFan: CeilingFan):
        self.ceilingFan = ceilingFan

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.high()

    def undo(self):
        if self.prevSpeed == CeilingFan.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.OFF:
            self.ceilingFan.off()


class CeilingFanMediumCommand(Command):
    def __init__(self, ceilingFan: CeilingFan):
        self.ceilingFan = ceilingFan

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.medium()

    def undo(self):
        if self.prevSpeed == CeilingFan.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.OFF:
            self.ceilingFan.off()


class CeilingFanOffCommand(Command):
    def __init__(self, ceilingFan: CeilingFan):
        self.ceilingFan = ceilingFan

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.off()

    def undo(self):
        if self.prevSpeed == CeilingFan.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.OFF:
            self.ceilingFan.off()


# receiver
class Light:
    def __init__(self, location):
        self.location = location

    def on(self):
        print(f'{self.location} light is on')

    def off(self):
        print(f'{self.location} light is off')


class CeilingFan:
    HIGH: int = 3
    MEDIUM: int = 2
    LOW: int = 1
    OFF: int = 0

    def __init__(self, location: str):
        self.location = location
        self.speed = self.OFF

    def high(self):
        self.speed = self.HIGH
        print(f'{self.location} ceiling fan is on high')

    def medium(self):
        self.speed = self.MEDIUM
        print(f'{self.location} ceiling fan is on medium')

    def low(self):
        self.speed = self.LOW
        print(f'{self.location} ceiling fan is on low')

    def off(self):
        self.speed = self.OFF
        print(f'{self.location} ceiling fan is on off')

    def getSpeed(self) -> int:
        return self.speed


# invoker
class RemoteControl:
    def __init__(self):
        noCommand = NoCommand()
        self.onCommands = [noCommand] * 7
        self.offCommands = [noCommand] * 7
        self.undoCommand = noCommand

    def setCommand(self, slot: int, onCommand: Command, offCommand: Command):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand

    def onButtonWasPressed(self, slot: int):
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]

    def offButtonWasPressed(self, slot: int):
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]

    def undoButtonWasPressed(self):
        self.undoCommand.undo()


remoteControl = RemoteControl()
kitchenLight = Light('kitchen')
livingRoomLight = Light('living room')
remoteControl.setCommand(0, LightOnCommand(kitchenLight), LightOffCommand(kitchenLight))
remoteControl.setCommand(1, LightOnCommand(livingRoomLight), LightOffCommand(livingRoomLight))
remoteControl.onButtonWasPressed(0)
remoteControl.undoButtonWasPressed()
remoteControl.onButtonWasPressed(1)
remoteControl.offButtonWasPressed(1)
ceilingFan = CeilingFan('living room')
remoteControl.setCommand(2, CeilingFanHighCommand(ceilingFan), CeilingFanOffCommand(ceilingFan))
remoteControl.setCommand(3, CeilingFanMediumCommand(ceilingFan), CeilingFanOffCommand(ceilingFan))
remoteControl.onButtonWasPressed(2)
remoteControl.onButtonWasPressed(3)
remoteControl.undoButtonWasPressed()
remoteControl.offButtonWasPressed(2)
