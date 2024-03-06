from collections import Counter
import math, random

def check_empty_list(getallen: list) -> dict:
    if not getallen:
        return {"Lijst is leeg, voer getallen in.":getallen}
    
def check_numeric1(controlegetal1:int) -> dict:
    if not str(controlegetal1).isnumeric():
        return {"Eerste controlle getal incorrect.":controlegetal1}
    
def check_numeric2(controlegetal2:int) -> dict:
    if not str(controlegetal2).isnumeric():
        return {"Eerste controlle getal incorrect.":controlegetal2}
    
def aantal(getallen: list) -> int:
    return len(getallen)

def bereken_som(getallen: list) -> int:
    return sum(getallen)

def gemiddelde(getallen: list) -> float:
    aantal_elementen = aantal(getallen)
    som_getallen = bereken_som(getallen)
    return som_getallen / aantal_elementen

def grootste_getal(getallen: list) -> int:
    return max(getallen)

def kleinste_getal(getallen: list) -> int:
    return min(getallen)

def eerste_getal(getallen: list) -> int:
    return getallen[0]

def delen1(kleinste_getal:int, controlegetal1:int) -> float:
    return kleinste_getal / controlegetal1

def delen2(grootste_getal:int, controlegetal1:int) -> float:
    return grootste_getal / controlegetal1

def unieke_getallen(getallen: list) -> list:
    return list(set(getallen))

def aantal_unieke_elementen(getallen: list) -> int:
    unieke_getallen_lijst = unieke_getallen(getallen)
    return len(unieke_getallen_lijst)

def bereken_verschil1(aantal_unieke_elementen:int, controlegetal1: int) -> int:
    return abs(aantal_unieke_elementen - controlegetal1)

def sorteer_lijst(getallen: list) -> list:
    return sorted(getallen)

def gesorteerde_lijst_uniek(unieke_getallen: int) -> list:
    return sorted(unieke_getallen)

def tel_elementen(getallen: list) -> dict:
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer
    return telling_elementen

def deelbare_getallen1(unieke_getallen:list, controlegetal1:int) -> list:
    deelbaar1 = []
    for getal in unieke_getallen:
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    deelbaar1 = sorted(deelbaar1)
    return deelbaar1

def deelbare_getallen2(unieke_getallen:list, controlegetal2:int) -> list:
    deelbaar2 = []
    for getal in unieke_getallen:
        if getal % controlegetal2 == 0:
            deelbaar2.append(getal)
    deelbaar2 = sorted(deelbaar2)
    return deelbaar2

def controleer_voorkomen(getallen: list, controlegetal1:int, controlegetal2:int):
    return controlegetal1 in getallen and controlegetal2 in getallen

def positie_controlegetal1(getallen:list, controlegetal1:int) -> list:
    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal1:
            posities.append(index)
    return posities

def bereken_standaardafwijking(getallen:list, gemiddelde:float) -> float:
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    aantal1 = aantal(getallen)
    variantie = verschil_kwadraat / aantal1
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking

def shuffle_lijst(getallen: list) -> list:
    lijst_shuffle = list(getallen)
    random.shuffle(lijst_shuffle)
    return lijst_shuffle

def kies_random_getal(getallen:list) -> int:
    aantal_getallen = aantal(getallen)
    random_getal = kies_random_getal(getallen)
    return getallen[random.randint(0,aantal_getallen-1)]

def bereken_verschil2(random_getal:int, controlegetal2: int) -> int:
    return abs(random_getal - controlegetal2)

def analyseer_getallenlijst(getallen:list, controlegetal1:int, controlegetal2:int) -> dict:
    resultaten = {
        "Aantal getallen": aantal(getallen),
        "Gemiddelde": gemiddelde(getallen),
        "Som": bereken_som(getallen),
        "Grootste getal": grootste_getal(getallen),
        "Kleinste getal": kleinste_getal(getallen),
        "Eerste getal": eerste_getal(getallen),
        f"{kleinste_getal(getallen)} / {controlegetal1}": delen1(kleinste_getal(getallen), controlegetal1),
        f"{grootste_getal(getallen)} / {controlegetal2}": delen2(grootste_getal(getallen), controlegetal2),
        "Aantal unieke elementen": aantal_unieke_elementen(getallen),
        f"Het verschil tussen {aantal_unieke_elementen(getallen)} & {controlegetal1}": bereken_verschil1(aantal_unieke_elementen(getallen), controlegetal1),
        "Gesorteerde lijst getallen": sorteer_lijst(getallen),
        "Gesorteerde lijst unieke getallen": gesorteerde_lijst_uniek(unieke_getallen(getallen)),
        "Telling van elementen": tel_elementen(getallen),
        f"Deelbaar door {controlegetal1} (op volgorde)": deelbare_getallen1(unieke_getallen(getallen), controlegetal1),
        f"Deelbaar door {controlegetal2} (op volgorde)": deelbare_getallen2(unieke_getallen(getallen), controlegetal2),
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": controleer_voorkomen(getallen, controlegetal1, controlegetal2),
        f"{controlegetal1} komt voor op positie(s)": positie_controlegetal1(getallen, controlegetal1),
        "Standaardafwijking": bereken_standaardafwijking(getallen, gemiddelde(getallen)),
        "Geshufflede lijst": shuffle_lijst(getallen),
        "Willekeurige getal uit de lijst": kies_random_getal(getallen),
        f"Het verschil tussen {kies_random_getal(getallen)} & {controlegetal2}": bereken_verschil2(kies_random_getal(getallen), controlegetal2),
    }
    return resultaten

getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")