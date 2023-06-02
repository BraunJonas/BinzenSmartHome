from Device import Device
class Room():
    name = ""
    devices = []
    def __init__(self, name:str):
        print("Room "+ name +" has been created")

    def getDevices(self):
        return self.devices

    def addDevice(self, device:Device):
        print("Device added to Room")
        self.devices.append(device)

    

            