from gegevens_opvragen import vragen_gegevens

#Naam, leeftijd en woonplaats (dictionaries(keys: 'name', 'age' en 'city')) worden omgezet in een lijst.
def verzamel_gegevens() -> list:
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
    print(f"In {data['city']} woont de {data['age']} jarige {data['name']}.")