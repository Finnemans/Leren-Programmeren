def check_even_numbers(number:int) -> bool:
    return number % 2 == 0 # deelt gegeven getal door 2 en als restwaarde 0 is geeft ie m terug

def reversed_string(string:str) -> str:
    woordjes = string.split() #split de tekst bij spaties slaar het op als woordjes
    reversed = woordjes[::-1] #draaid de gegeven woordjes van achterstevoren = hallo allemaal word: allemaal hallo
    reversed_string = ' '.join(reversed) #plakt ze samen als 1 string
    return reversed_string

def aantal_nummers(nummers:str) -> int:
    nummers_los = set(nummers) # een getal word gesplitst in nummers als 123 naar {'1', '2', '3'}
    aantal_nummers = len(nummers_los) #hier pakt ie hoeveel nummers er zijn 
    return aantal_nummers

def gemiddelde_woordlengte(zin: str) -> float:
    woorden = zin.split() #split de woorden
    
    totaal_lengte = 0
    for woord in woorden: #de woorden af
        totaal_lengte += len(woord) #telt letters van elk woord bij totaal lenggte op
    
    gemiddelde = totaal_lengte / len(woorden) #gemiddelde is aantal woorden delen door alle lengtes
    return gemiddelde

def vermenigvuldig_tafel(getal: int, max_factor: int = 10) -> None:
    for factor in range(1, max_factor + 1): # loop van 1 tot 12
        resultaat = factor * getal #resultaat = poging in loop * getal
        print(f'{factor} x {getal} = {resultaat}')