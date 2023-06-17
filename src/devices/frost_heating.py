from devices.device import Device
from actors.switch_on_offable import SwitchOnOffable


class FrostHeating(Device, SwitchOnOffable):
    __instance = None
     #Singleton
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print("New Frostheating instance is created")
            cls.__instance = super().__new__(cls)
        else:
            print("Frostheating already existed: instance returned")
        return cls.__instance

    def __init__(self):
        if(type(self).__instance is None):
            super().__init__("Frostheating")
            type(self).__instance.running = False

        

    def setRunning(self, running: int):
        self.running = running
        print("FrostHeating set running to " + str(running))

    def isRunning(self) -> bool:
        return self.running
    
    def simuliereEinenThreadDurchlauf(self):
        #ask weather station for the wether
        # decide wether to set myself running or not
        print(f"ShadowingDevice {self.name} is {'running ' if self.running else 'not running'}" )