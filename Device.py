class Device():
    name = ""
    def __init__(self, name:str):
        self.name = name

    def getName(self) -> str:
        return self.name
    
    def setName(self, name:str):
        self.name = name