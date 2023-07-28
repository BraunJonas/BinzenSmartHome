from typing import Dict, Any

from rooms.zone import Zone

class ZonePrototypeRegister():
        ## SRP -> PrototypeRegister hat nur die Aufgabe Prototypes zu verwalten -> Getrennt von der Klasse Gardenhousezone
        __prototypes: dict[Zone, str] = {}

        @staticmethod
        def addPrototype(prototype: Zone, name: str):
            ZonePrototypeRegister.__prototypes.update({name: prototype})

        @staticmethod
        def deletePrototype(name: str):
            print("bb")
            ZonePrototypeRegister.__prototypes.pop(name)

        @staticmethod
        def getPrototype(name: str):
            return ZonePrototypeRegister.__prototypes[name]

        @staticmethod
        def getPrototypes():
            return ZonePrototypeRegister.__prototypes.keys()
