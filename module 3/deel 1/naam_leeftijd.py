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

def verzamel_gegevens():
    gegevens_list = []
    gegevens = vragen_gegevens()
    gegevens_list.append(gegevens)
    while True:
        invoer = input("Toets enter om door te gaan of stop om te printen: ").lower()
        if invoer == "stop":
            break
        elif invoer == "":
            gegevens = vragen_gegevens()
            gegevens_list.append(gegevens)
        else:
            print("Ongeldige invoer. Toets alstublieft op enter of voer 'stop' in.")

    return gegevens_list

gegevens = verzamel_gegevens()

for data in gegevens:
    print(f"{data['name']}, die in {data['city']} woont, is {data['age']} jaar.")