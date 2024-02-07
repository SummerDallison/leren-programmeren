shopping_list = {}

while True:
    item = input("Welke item wilt u toevoegen aan uw booschappenlijstje? ").lower()
    if not item:
        print("U hebt nog geen item ingevoerd.")
        continue

    if item in shopping_list:
        shopping_list[item] += 1
    else:
        shopping_list[item] = 1

    while True:
        more_items = input("Wil je nog meer items toevoegen aan uw boodschappenlijstje? (ja/nee) ").lower()

        if more_items.lower() == "nee":
            print(" --- [Boodschappenlijst] --- ")
            for item, quantity in shopping_list.items():
                print(f"{quantity}x {item}")
            break

        elif more_items != 'ja':
            print("Voer alstublieft 'ja' of 'nee' in.")
            continue

        else:
            break