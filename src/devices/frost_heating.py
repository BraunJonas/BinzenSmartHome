from devices.device import Device
from actors.switch_on_offable import SwitchOnOffable


class FrostHeating(Device, SwitchOnOffable):
    __instance = None
     #Singleton

    def __init__(self):
        if FrostHeating.__instance != None:
            raise Exception("This is a Singleton class")
        super().__init__("Frostheating")
        self.running = False
        FrostHeating.__instance = self

    @staticmethod
    def getInstance():
        if FrostHeating.__instance == None:
            print("Creating new FrostHeatig instance")
            FrostHeating()
        else:
            print("Instance already existed: returning instance")
        return FrostHeating.__instance


    def setRunning(self, running: int):
        self.running = running
        print("FrostHeating set running to " + str(running))

    def isRunning(self) -> bool:
        return type(self).__instance.running
    
    def simuliereEinenThreadDurchlauf(self):
        #ask weather station for the weather
        # decide wether or not to set myself running 
        print(f"FrostHeating {self.name} is {'running ' if self.running else 'not running'}" )