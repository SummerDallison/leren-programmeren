import random

deelnemers = []

while len(deelnemers) < 3:
    naam = input("Voer de naam van een deelnemer in: ").lower()

    if naam.isalpha():
        if naam not in deelnemers:
            deelnemers.append(naam)
            print(f"De naam '{naam}' is toegevoegd aan de lootjes.")
        
        else:
            print(f"De naam {naam} is al toegevoegd aan de lootjes. Deze naam wordt niet opnieuw toegevoegd.")

    else:
        print("Ongeldige invoer. Voer alstublieft alleen letters in voor de naam.")

while True:
    meer_toevoegen = input("Wilt u meer deelnemers toevoegen? (ja/nee): ").lower()

    if meer_toevoegen == "ja":
        while True:
            naam = input("Voer de naam van een deelnemer in: ").lower()

            if naam.isalpha():
                if naam not in deelnemers:
                    deelnemers.append(naam)
                    print(f"De naam '{naam}' is toegevoegd aan de lootjes.")
            
                else:
                    print(f"De naam {naam} is al toegevoegd aan de lootjes. Deze naam wordt niet opnieuw toegevoegd.")

            else:
                print("Ongeldige invoer. Voer alstublieft alleen letters in voor de naam.")
                continue
            break

    elif meer_toevoegen == "nee":
        break

    else:
        print("Voer alstublieft 'ja' of 'nee' in.")

while True:
    lootjes = deelnemers.copy()
    random.shuffle(lootjes)

    print("De lootjes worden nu gecontroleerd en verdeeld.")

    if all(deelnemer != lootje for deelnemer, lootje in zip(deelnemers, lootjes)):
        break

for deelnemer, lootje in zip(deelnemers, lootjes):
    print(f"{deelnemer} trekt lootje van {lootje}.")