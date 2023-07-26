#Da keine Wetterstation zur Verfügung steht wurde ihre Funktionalität hier für zwei Beispiele simulier

from random import randint


def getExpectedTemp() -> [int, int]:
    min = randint(-10, 30)
    max = randint(min, 40)
    return min, max

def getExpectedRainAmount() -> int:
    return randint(0, 30)
