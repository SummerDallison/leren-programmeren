import random

deelnemers = []
cadeau_wensen = {}

def input_yes_no(prompt):
    while True:
        antwoord = input(prompt + " (ja/nee): ").lower()
        if antwoord in ('ja', 'nee'):
            return antwoord == 'ja'
        print("Ongeldige invoer. Voer alstublieft 'ja' of 'nee' in.")

def input_string(prompt):
    while True:
        waarde = input(prompt).capitalize()
        if waarde.isalpha():
            return waarde
        print("Ongeldige invoer. Voer alstublieft alleen letters in.")

def input_cadeauwensen(naam):
    wensen = []
    for i in range(3):
        wens = input(f"Voer cadeauwens {i+1} in voor {naam}: ")
        wensen.append(wens)
    return wensen

def voeg_deelnemer_toe(deelnemers, cadeau_wensen):
    naam = input_string("Voer de naam van een deelnemer in: ")
    if naam not in deelnemers:
        deelnemers.append(naam)
        print(f"De naam '{naam}' is toegevoegd aan de lootjes.")
        cadeau_wensen[naam] = input_cadeauwensen(naam)
    else:
        print(f"De naam {naam} is al toegevoegd aan de lootjes. Deze naam wordt niet opnieuw toegevoegd.")

def verdelen_lootjes(deelnemers):
    while True:
        lootjes = deelnemers.copy()
        random.shuffle(lootjes)
        if all(deelnemer != lootje for deelnemer, lootje in zip(deelnemers, lootjes)):
            return dict(zip(deelnemers, lootjes))
        
def opvragen_lootje(deelnemers_lootjes, cadeau_wensen):
    lootje_opvragen = input_string("Voer de naam in van een deelnemer in om het lootje op te vragen: ")
    if lootje_opvragen in deelnemers_lootjes:
        lootje = deelnemers_lootjes[lootje_opvragen]
        print(f"Het lootje van {lootje} is gekoppeld aan {lootje_opvragen}.")
        print(f"Cadeauwensen van {lootje}: ")
        for cadeau, wens in enumerate(cadeau_wensen[lootje], 1):
            print(f"{cadeau}. {wens}")
    else:
        print("Deze naam staat niet op de lijst van deelnemers.")