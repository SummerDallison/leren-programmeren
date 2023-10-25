print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">          Amnesia in the Realm of Enchantment          >")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

naam = input("Voer uw naam in: ")
while not naam.isalpha():
        print("Ongeldige invoer. Voer alleen letters in uw naam.")
        naam = input("Voer uw naam in: ")

bevestiging_naam = input(f"Uw naam is {naam}, klopt dit? (ja/nee): ")
while bevestiging_naam.lower() != "ja":
    naam = input("Voer uw naam in: ")
    bevestiging_naam = input(f"Uw naam is {naam}, klopt dit? (ja/nee): ")

leeftijd = input("Voer uw leeftijd in: ")

while True:
    try:
        leeftijd = int(leeftijd)
        if leeftijd >= 0:
            leeftijd_bevestiging = input(f"Uw leeftijd is {leeftijd}, klopt dit? (ja/nee): ")
            if leeftijd_bevestiging.lower() == "ja":
                break
            else:
                leeftijd = input("Voer uw leeftijd in: ")
        else:
            print("Ongeldige invoer. Voer een positieve numerieke leeftijd in.")
            leeftijd = input("Voer uw leeftijd in: ")        
    except ValueError:
        print("Ongeldige invoer. Voer een numerieke leeftijd in.")
        leeftijd = input("Voer uw leeftijd in: ")

print("")