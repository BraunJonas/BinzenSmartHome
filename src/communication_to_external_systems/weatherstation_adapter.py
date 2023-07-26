#Adapter Design Pattern -> Anpassung der Daten der externen Wetterstation an die benötigte Struktur
import src.communication_to_external_systems.weatherstation

def getMinExpectedTemp() -> int:
    return src.communication_to_external_systems.weatherstation.getExpectedTemp()[0]

def getExpectedRainAmount() -> int:
    return src.communication_to_external_systems.weatherstation.getExpectedRainAmount()
