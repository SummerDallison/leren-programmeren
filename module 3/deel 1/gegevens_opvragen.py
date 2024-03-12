def vragen_gegevens():
    while True:
        naam = input("Voer uw naam in: ")
        if naam.isalpha():
            break
        else:
            print("Ongeldige invoer. Voer alstublieft uw naam in.")

    while True:
        leeftijd = input("Voer uw leeftijd in: ")
        if leeftijd.isdigit():
            break
        else:
            print("Ongeldige invoer. Voer alstublieft uw leeftijd in.")

    while True:
        woonplaats = input("Voer uw woonplaats in: ")
        if woonplaats.isalpha():
            break
        else:
            print("Ongeldige invoer. Voer alstublieft uw woonplaats in.")

    return {'name' : naam, 'age' : leeftijd, 'city' : woonplaats}