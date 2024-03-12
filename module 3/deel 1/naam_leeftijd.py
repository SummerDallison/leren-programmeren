def vraag_naam_en_leeftijd():
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

    return {'name' : naam, 'age' : leeftijd}

gegevens = vraag_naam_en_leeftijd()

print(f"{gegevens['name']} is {gegevens['age']} jaar.")