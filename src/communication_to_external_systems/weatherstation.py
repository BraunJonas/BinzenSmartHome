#Da keine Wetterstation zur Verfügung steht wurde ihre Funktionalität hier für zwei Beispiele simulieren

from random import randint


def getExpectedTemp() -> [int, int]:#zu erwartende Temperatur
    min = randint(-10, 30)
    max = randint(min, 40)
    return min, max

def getExpectedRainAmount() -> int:#zu erwartender Niederschlag
    return randint(0, 30)
