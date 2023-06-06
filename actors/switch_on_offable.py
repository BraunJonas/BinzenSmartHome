from actor import Actor


class SwitchOnOffAble(Actor):
    running = False

    def setRunning(self, running: bool):
        self.running = running

    def isRunning(self) -> bool:
        return self.running
