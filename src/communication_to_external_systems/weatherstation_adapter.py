#Adapter Design Pattern -> Anpassung der Daten der externen Wetterstation an die benötigte Struktur
#Da keine Wetterstation zur Verfügung steht wurde die Funktionalität hier ohne einen zugriff auf die Wetterstation simuliert.
from random import randint


def getMinExpectedTemp() -> int:
    return randint(-10,30)

def getExpectedRainAmount() -> int:
    return randint(0,30)
