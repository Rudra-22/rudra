from abc import ABC, abstractmethod

class DeviceBase(ABC):
    def __init__(self, name):
        self._status = False
        self._name = name

    def show_status(self):
        print(f"{self._name} is {'ON' if self._status else 'OFF'}")

    def is_on(self):
        return self._status

    def set_status(self, state):
        self._status = state

    @abstractmethod
    def operate(self):

class Light(DeviceBase):
    def __init__(self, label):
        super().__init__(label)
        self.__brightness = 0.7 

    def operate(self):
        if self.is_on():
            self.set_status(False)
            print(f"{self._name} light turned off")
        else:
            self.set_status(True)
            print(f"{self._name} light turned on at {int(self.__brightness*100)}% brightness")

    def get_brightness(self):
        return self.__brightness

    def set_brightness(self, value):
        if 0 <= value <= 1:
            self.__brightness = value
        else:
            raise ValueError("Brightness should be between 0 and 1")

class Fan(DeviceBase):
    def __init__(self, tag):
        super().__init__(tag)
        self.__speed = "medium"

    def operate(self):
        if self.is_on():
            self.set_status(False)
            print(f"{self._name} fan stopped")
        else:
            self.set_status(True)
            print(f"{self._name} fan spinning at {self.__speed} speed")

    def get_speed(self):
        return self.__speed

    def set_speed(self, level):
        if level in ["low", "medium", "high"]:
            self.__speed = level
        else:
            raise ValueError("Speed must be low, medium or high")

class AirConditioner(DeviceBase):
    def __init__(self, ident):
        super().__init__(ident)
        self.__temperature = 24  

    def operate(self):
        if self.is_on():
            self.set_status(False)
            print(f"{self._name} AC turned off")
        else:
            self.set_status(True)
            print(f"{self._name} AC cooling at {self.__temperature}°C")

    def get_temp(self):
        return self.__temperature

    def set_temp(self, temp_val):
        if 16 <= temp_val <= 30:
            self.__temperature = temp_val
        else:
            raise ValueError("Temp should be between 16 and 30")

def demo_home():
    light1 = Light("Living Room")
    fan1 = Fan("Main Fan")
    ac1 = AirConditioner("Bedroom AC")

    for device in [light1, fan1, ac1]:
        device.operate()
        device.show_status()

  
