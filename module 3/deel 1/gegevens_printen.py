from gegevens_opvragen import vragen_gegevens

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