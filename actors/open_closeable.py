from actor import Actor

class OpenCloseable(Actor):
    open = False

    def isOpen(self) -> bool:
        return self.open    
    
    def setOpen(self, open:bool):
        self.open = open
        