from src.rooms.zone import Zone

class ZonePrototypeRegister():
        ## SRP -> PrototypeRegister hat nur die Aufgabe Prototypes zu verwalten -> Getrennt von der Klasse Gardenhousezone
        __prototypes = {}

        @staticmethod
        def addPrototype(prototype: Zone, name: str):
            ZonePrototypeRegister.__prototypes.update({name: prototype})
            print(ZonePrototypeRegister.__prototypes[name])

        @staticmethod
        def deletePrototype(name: str):
            ZonePrototypeRegister.__prototypes.pop(name)

        @staticmethod
        def getPrototype(name: str):
            return ZonePrototypeRegister.__prototypes[name]
