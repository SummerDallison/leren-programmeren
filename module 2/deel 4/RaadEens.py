import random
score = 0

for rondes in range(1, 21):
    print(f"\nRonde {rondes}: ")
    geheimGetal = random.randint(1, 1000)
    
    for pogingen in range(1, 11):
        while True:
            try:
                getalRaden = int(input(f"\nPoging {pogingen}: Raad een getal tussen de 1 en de 1000: "))
                if getalRaden < 1 or getalRaden > 1000:
                    print("Voer alstublieft een getal in tussen de 1 en de 1000.")
                
                else:
                    break

            except ValueError:
                print("Voer alstublieft een geldig getal in tussen de 1 en de 1000.")

        if getalRaden == geheimGetal:
            print("Gefeliciteerd! Je hebt het juiste getal geraden. ")
            score += 1
            break

        elif getalRaden < geheimGetal:
            print("Hoger!")

        else:
            print("Lager!")

        verschil = abs(getalRaden - geheimGetal)

        if verschil < 20:
            print("Je bent heel warm!")
        elif verschil < 50:
            print("Je bent warm!")

    print(f"Het geheime getal was: {geheimGetal}")
    print(f"Score tot nu toe: {score}/20\n")

    if rondes < 20:
        while True:
            volgendeRonde = input("\nEen nieuwe ronde starten? (ja/nee): ").lower()

            if volgendeRonde == "ja" or volgendeRonde == "nee":
                break

            else:
                print("Voer alstublieft 'ja' of 'nee' in.")
        
        if volgendeRonde == "nee":
            break

print(f"Eindscore: {score}/20")