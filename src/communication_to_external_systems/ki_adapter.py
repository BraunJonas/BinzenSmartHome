#Adapter für die externe Schnittstellenkommunikation zu floraGPT
from communication_to_external_systems.floraGPT import ermittlePflegehinweis

def getPflegeHinweis(bild: str) -> str:
    hinweis = ermittlePflegehinweis(bild) #Pfleehinweisermittlung für KI
    code = hinweis[5:8] #Anpassung des returns zur Weiterverarbeitung
    if code=="000" or code =="999":
        raise KIError #'000' : 'Systemausfall' , '999' : 'Antwortzeit zu lang' 
    return code 

class KIError(Exception):
    pass
