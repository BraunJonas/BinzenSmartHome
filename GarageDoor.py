import OpenCloseAble

class GarageDoor(OpenCloseAble):

    def __init__(self, open:bool):
        super.__init__(open)
        self.open : bool

    def get_open(self) -> bool:
        return self.open
    




