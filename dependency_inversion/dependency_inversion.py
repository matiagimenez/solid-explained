"""
Dependency Inversion (DIP) - “Don't trust anyone below you!” 
"""

class LightBulb:
    def turn_on(self):
        print("LightBulb: Turning on")

    def turn_off(self):
        print("LightBulb: Turning off")
"""
Before applying Dependency Inversion Principle (DIP), the Switch class directly depends on the LightBulb class.
If we want to add another device, say LEDLight, we'd have to modify the Switch class, which violates the Open/Closed Principle as well.
"""

class Switch:
    def __init__(self, bulb: LightBulb):
        self.bulb = bulb  # Directly depends on the concrete implementation of LightBulb

    def operate(self):
        print("Switch: Operating")
        self.bulb.turn_on()  # Directly calls the method on LightBulb



"""
After applying Dependency Inversion Principle (DIP), the Switch class now depends on the abstraction `Switchable` (an interface), not on any specific implementation of devices 
like LightBulb or LEDLight.

This allows the Switch to work with any device that implements the `Switchable` interface.
"""

from abc import ABC, abstractmethod

class Switch:
    def __init__(self, device: 'Switchable'):
        self.device = device  # The switch now accepts any device that can be switched on/off.

    def operate(self):
        """
        The operate method will call `turn_on()` on the device passed into the constructor.
        This way, Switch does not care whether it's a LightBulb, LEDLight, or any other device.
        """
        print("Switch: Operating")
        self.device.turn_on()  # Delegate the operation to the passed device (light bulb, LED light, etc.)

class Switchable(ABC):
    """
    `Switchable` is an abstraction that ensures any device that is controlled by the Switch
    can be turned on or off. The high-level `Switch` class depends on this abstraction,
    not the concrete device.
    """
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    """
    LightBulb is a concrete implementation of the `Switchable` interface.
    It implements the methods `turn_on` and `turn_off`.
    """
    def turn_on(self):
        print("LightBulb: Turning on")

    def turn_off(self):
        print("LightBulb: Turning off")


class LEDLight(Switchable):
    """
    LEDLight is another concrete implementation of the `Switchable` interface.
    It also provides its own version of `turn_on` and `turn_off` methods.
    """
    def turn_on(self):
        print("LEDLight: Turning on")

    def turn_off(self):
        print("LEDLight: Turning off")