from Aktor import Aktor

class OpenCloseAble(Aktor):
    open = False

    def isOpen(self) -> bool:
        return self.open    
    
    def setOpen(self, open:bool):
        self.open = open
        