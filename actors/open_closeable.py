from actor import Actor


class OpenCloseAble(Actor):
    open = False

    def isOpen(self) -> bool:
        return self.open

    def setOpen(self, open: bool):
        self.open = open
