# REP - alle Klassen des Actors Packages sind wiederverwendbar

# CRP - die Klassen des Actors Packages werden zusammen wiederverwendet

# SAP - Stabilität wächst in Richtung der Abstraktheit - Interfaces sind stbil und abstrakt

# OCP - offen für Erweiterungen, geschlossen für Modifikationen: 
# Alle Geräte können mehrere Actor-Interfaces implementieren, es ist leicht zusätzliche Funktionen hinzuzufügen

# ISP - Aufteilung von Funktionen und Zuordnung zu spezifischen Klassen: 
# Mehrere abstrakte Klassen, die jeweils spezifische Funktionen implementieren,
# damit Klassen nur Methoden implementieren die sie tatsächlich benötigen und übermäßige Abhängigkeit verhindern

class OpenCloseable():
    def isOpen(self) -> bool:
        raise NotImplementedError    
    
    def setOpen(self, open:bool):
        raise NotImplementedError
        