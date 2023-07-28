from typing import List
import datetime
import logging
from controller import Controller
from rooms.gardenhouse_zone import GardenhouseZone
from rooms.zone import Zone
from rooms.zone_prototype_register import ZonePrototypeRegister


# ADP - Es gibt keine Zyklen in der Abhängigkeitsstruktur des gesamten Codes

def setUpLogger():
    logging.basicConfig(filename="SmartHomeLog.log", encoding="utf-8", level=logging.DEBUG)
    logger = logging.getLogger()
    logger.info(10*"-" + str(datetime.datetime.now()) + 75*"-")

def ask_yesno(question):
    yes = {'yes', 'y', 'j', 'ja'}
    no = {'no', 'n', 'nein'}

    done = False
    print(question)
    while not done:
        choice = input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print("Bitte antworte mit ja oder nein.")

def showMenu(title: str, options: List[str]):
    while (True):
        print(title)
        ctr = 1
        for s in options:
            print("\t" + str(ctr) + " " + s)
            ctr = ctr+1
        eingabe = input()
        if(eingabe == "q"):
            print("Menu wird verlassen")
            return -1
        try:
            number = int(eingabe)
            if (number < ctr and number>0):
                return number-1
        except ValueError:
            pass
        print("Gib eine gültige Zahl ein")


#eventuell in zweiter datei laden?
def askChanges():
    while(True):
        if ask_yesno("Möchten Sie weitere Einstellungen ändern, Devices oder Zonen hinzufügen? [y/n]"):
            print("Zum Verlassen des Menus drücke Q")
            chooseZone()
        else:
            break

def chooseZone():
    options = []
    for z in Controller.getZones():
        options.append(z.getName())
    options.append("Neuen Raum hinzufügen")
    chosenOption = showMenu("Wähle eine Zone aus, die du verändern möchtest:", options)
    if(chosenOption < 0):
        return
    elif chosenOption == len(options) -1:
        addZone()
    else:
        chooseDevice(chosenOption)


def addDevice(zone: int):
    print("Gib einen Namen für das neue Device ein: ")
    name = input()
    if (name == "q"):
        return
    options = Controller.getDeviceOptions()
    chosenOption = showMenu("Wähle eine Device aus, welches du erstellen möchtest", options)
    if (chosenOption < 0):
        return
    Controller.addDevice(zone, options[chosenOption], name)
    print("Device mit Standardeinstellungen hinzugefügt")



def changePercentage(zone, device):
    while (True):
        print("Gib einen neuen Wert ein")
        eingabe = input()
        if (eingabe == "q"):
            print("Menu wird verlassen")
        try:
            number = int(eingabe)
            if number <= 100 and number >= 0:
                Controller.changePercentage(zone, device, number)
                break
        except ValueError:
            pass
        print("Gib einen gültigen Wert ein")
    print("Prozentangabe verändert - Änderung kann im Logfile eingesehen werden")


def changeTemp(zone, device):
    while (True):
        print("Gib einen neuen Wert ein")
        eingabe = input()
        if (eingabe == "q"):
            print("Menu wird verlassen")
        try:
            number = int(eingabe)
            if number >= 0:
                Controller.changeTemp(zone, device, number)
                break
        except ValueError:
            pass
        print("Gib einn gültigen Wert ein")
    print("Temperatur verändert - Änderung kann im Logfile eingesehen werden")



def changeAmount(zone, device):
    while (True):
        print("Gib einen neuen Wert ein")
        eingabe = input()
        if (eingabe == "q"):
            print("Menu wird verlassen")
        try:
            number = int(eingabe)
            if (number >= 0):
                Controller.changeAmount(zone, device, number)
                break
        except ValueError:
            pass
        print("Gib einn gültigen Wert ein")
    print("Menge verändert - Änderung kann im Logfile eingesehen werden")



def changeAudio(zone, device):
    print("Gib einen Dateinamen ein: ")
    eingabe = input()
    if (eingabe == "q"):
        print("Menu wird verlassen")
    Controller.changeAudio(zone, device, eingabe)
    print("Audio verändert - Änderung kann im Logfile eingesehen werden")


def changeVideo(zone, device):
    print("Gib einen Dateinamen ein: ")
    eingabe = input()
    if eingabe == "q":
        print("Menu wird verlassen")
    Controller.changeVideo(zone, device, eingabe)
    print("Video verändert - Änderung kann im Logfile eingesehen werden")


def changeName(zone, device):
    print("Gib einen Namen ein: ")
    eingabe = input()
    if eingabe == "q":
        print("Menu wird verlassen")
    Controller.changeName(zone, device, eingabe)
    print("Name geändert")


def changeDevice(zone, device):
    optionsTupel = Controller.getChangeOptions(zone, device)
    options = []
    for o in optionsTupel:
        options.append(o[1])
    chosenOption = showMenu("Wähle aus, was du verändern möchtest", options)
    if (chosenOption < 0):
        return
    match optionsTupel[chosenOption][0]:
        case 0:
            changePercentage(zone, device)
        case 1:
            changeTemp(zone, device)
        case 2:
            changeAmount(zone, device)
        case 3:
            Controller.invertOpen(zone,device)
            print("Attribut Open wurde invertiert - Änderungen können im Logfile eingesehen werden")
        case 4:
            Controller.invertRunning(zone,device)
            print("Attribut Running wurde invertiert - Änderungen können im Logfile eingesehen werden")
        case 5:
            Controller.invertLocked(zone,device)
            print("Attribut Locked wurde invertiert - Änderungen können im Logfile eingesehen werden")
        case 6:
            Controller.invertReactToAlarms(zone, device)
            print("Attribut ReactToAlarms wurde invertiert - Änderungen können im Logfile eingesehen werden")
        case 7:
            changeAudio(zone, device)
        case 8:
            changeVideo(zone, device)
        case 9:
            changeName(zone, device)
        case 10:
            Controller.deleteDevice(zone, device)
            print("Device wurde gelöscht")


def chooseDevice(zone: int):
    options = []
    for d in Controller.getDevices(zone):
        options.append(d.getName())
    options.append("Neues Device hinzufügen")
    chosenOption = showMenu("Wähle ein Device aus, das du verändern möchtest:", options)
    if (chosenOption < 0):
        return
    elif chosenOption == len(options) - 1:
        addDevice(zone)
    else:
        changeDevice(zone,chosenOption)

def addZone():
    print("Gib einen Namen für die neue Zone ein: ")
    name = input()
    if(name == "q"):
        return
    options = []
    for z in ZonePrototypeRegister.getPrototypes():
        options.append(z)
    options.append("Empty GardenhouseZone")
    options.append("Empty Zone")
    chosenOption = showMenu("Wähle einen Prototype aus, nach dem du deine Zone aufbauen möchtest:", options)
    if (chosenOption < 0):
        return
    elif chosenOption == len(options) -1:
        Controller.addZone(Zone(name))
    elif chosenOption == len(options) -2:
        Controller.addZone(GardenhouseZone(name))
    else:
        Controller.addZone(ZonePrototypeRegister.getPrototype(options[chosenOption]).clone(name))
    print("Zone hinzugefügt")



if __name__ == "__main__":
    setUpLogger()
    Controller.setUp()
    while(True):
        print("Das Smarthomesystem simuliert einen Threaddurchlauf - Änderungen können im Logfile eingesehen werden")
        Controller.simuliereEinenThreadDurchlauf()
        askChanges()










        
   


