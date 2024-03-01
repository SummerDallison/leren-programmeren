def even_getal(getal:int) -> bool:
    return getal % 2 == 0 
#Deze functie checkt of het getal even is (even: True, oneven: False).

def omgekeerde_woorden(zin:str) -> str:
    woorden = zin.split()
    doldwaze_broccoli = woorden[::-1]
    omgekeerde_zin = ' '.join(doldwaze_broccoli)
    return omgekeerde_zin 
#Deze functie keert de volgorde van woorden in de gegeven zin om.

def unieke_karakters(tekst:str) -> int:
    unieke_karakters_set = set(tekst)
    aantal_unieke_characters = len(unieke_karakters_set)
    return aantal_unieke_characters
#Deze functie telt alle letters op, maar het zijn alleen de letters die nog niet opgeteld zijn (geen dubbele letters).

def gemiddelde_woordenlengte(zin:str) -> float:
    woorden = zin.split()
    
    totaal_karakters = 0
    for woord in woorden:
        totaal_karakters += len(woord)

    gemiddelde = totaal_karakters / len(woorden)
    return gemiddelde
#Deze functie berekent het gemiddelde aantal karakters per woord in de zin.

def print_vermenigvuldigingstabel(getal:int, aantal_keer:int=10) -> None:
    for vermenigvuldiger in range(1, aantal_keer+1):
        resultaat = vermenigvuldiger * getal
        print(f'{vermenigvuldiger} x {getal} = {resultaat}')
#Deze functie print de vermenigvuldigingstabel tot 10 en met het gegeven getal.