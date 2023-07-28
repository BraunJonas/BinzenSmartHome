#Adapter Design Pattern -> Anpassung der Daten der externen Wetterstation an die benötigte Struktur
import communication_to_external_systems.weatherstation

def getMinExpectedTemp() -> int:
    return communication_to_external_systems.weatherstation.getExpectedTemp()[0]

def getExpectedRainAmount() -> int:
    return communication_to_external_systems.weatherstation.getExpectedRainAmount()
