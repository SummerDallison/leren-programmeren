import random

deelnemers = []
cadeau_wensen = {}

#Functie om ja/nee vragen te stellen
def input_yes_no(prompt):
    while True:
        antwoord = input(prompt + " (ja/nee): ").lower()
        if antwoord in ('ja', 'nee'):
            return antwoord == 'ja'
        print("Ongeldige invoer. Voer alstublieft 'ja' of 'nee' in.")

#Functie om een string in te voeren die alleen letters bevat
def input_string(prompt):
    while True:
        waarde = input(prompt).capitalize()
        if waarde.isalpha():
            return waarde
        print("Ongeldige invoer. Voer alstublieft alleen letters in.")

#functie om cadeauwensen in te voeren
def input_cadeauwensen(naam):
    wensen = []
    for i in range(3):
        while True:
            wens = input(f"Voer cadeauwens {i+1} in voor {naam}: ").lower().strip()
            if not wens:
                print("Er is geen cadeauwens ingevoerd. Voer alstublieft een wens in.")
            elif wens in wensen:
                print("Deze cadeauwens is al ingevoerd. Voer alstublieft een andere wens in.")
            elif not any(char.isalpha() for char in wens):
                print("Geen geldige cadeauwens ingevoerd. Voer alstublieft een geldige wens in.")
            else:
                wensen.append(wens)
                break
    return wensen

#Functie om een deelnemer toe te voegen
def voeg_deelnemer_toe(deelnemers, cadeau_wensen):
    naam = input_string("Voer de naam van een deelnemer in: ")
    if naam not in deelnemers:
        deelnemers.append(naam)
        print(f"De naam '{naam}' is toegevoegd aan de lootjes.")
        cadeau_wensen[naam] = input_cadeauwensen(naam)
    else:
        print(f"De naam {naam} is al toegevoegd aan de lootjes. Deze naam wordt niet opnieuw toegevoegd.")

#Functie om de lootjes te verdelen
def verdelen_lootjes(deelnemers):
    while True:
        lootjes = deelnemers.copy()
        random.shuffle(lootjes)
        if all(deelnemer != lootje for deelnemer, lootje in zip(deelnemers, lootjes)):
            return dict(zip(deelnemers, lootjes))

#Functie om het lootje van een deelnemer op te vragen        
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