deelnemers = []
cadeau_wensen = {}

def deelnemer_toevoegen(naam: str) -> str:
    if naam.isalpha():
        if naam not in deelnemers:
            deelnemers.append(naam)
            print(f"De naam '{naam}' is toegevoegd aan de lootjes.")   
            vraag_cadeau_wensen(naam)
        else:
            print(f"De naam {naam} is al toegevoegd aan de lootjes. Deze naam wordt niet opnieuw toegevoegd.")    
    else:
        print("Ongeldige invoer. Voer alstublieft alleen letters in voor de naam.")


def vraag_cadeau_wensen(naam: str) -> str:
    wensen = []
    for cadeau in range(3):
        wens = input(f"Voer cadeauwens {cadeau+1} in voor {naam}: ")
        wensen.append(wens)
    cadeau_wensen[naam] = wensen