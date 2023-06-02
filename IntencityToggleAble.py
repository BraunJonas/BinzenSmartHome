from Aktor import Aktor

class IntencityToggleAble( Aktor):

    intencity =0

    def getIntencity(self) -> int:
        return self.intencity    
    
    def setIntencity(self, intencity:int):
        if ( intencity > 100 or intencity < 0):
            raise Exception("not possible")
        self.intencity = intencity