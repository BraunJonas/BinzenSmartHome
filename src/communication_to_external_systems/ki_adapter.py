from src.communication_to_external_systems.floraGPT import ermittlePflegehinweis

def getPflegeHinweis(bild: str) -> str:
    hinweis = ermittlePflegehinweis(bild)
    code = hinweis[5:8]
    if code=="000" or code =="999":
        raise KIError
    return code

class KIError(Exception):
    pass
