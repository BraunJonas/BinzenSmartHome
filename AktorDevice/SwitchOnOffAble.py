from Aktor import Aktor

class SwitchOnOffAble(Aktor):
    running = False
        
    def setRunning(self, running:bool):
        self.running = running 

    def isRunning(self) -> bool:
        return self.running