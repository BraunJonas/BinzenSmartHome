import Light

class ColorLight(Light):
    def __init__(self, color:str):
        self.color = color
    
    def getColor(self)-> str:
        return self.color
    
    def setColor(self, color:str):
        self.color = color