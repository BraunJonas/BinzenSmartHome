from actor import Actor

class SwitchOnOffable(Actor):
    running = False
        
    def setRunning(self, running:bool):
        self.running = running 

    def isRunning(self) -> bool:
        return self.running