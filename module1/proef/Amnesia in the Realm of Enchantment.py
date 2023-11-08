print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">          Amnesia in the Realm of Enchantment          >")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

inventaris = []
companions = []
profiel_inhoud = []

print("Ik word langzaam wakker en knijp mijn ogen samen in een poging om te wennen aan het\nverblindende zonlicht dat mijn zicht overweldigt.")
print("Ik kijk verward om me heen en besef dat ik op een onbekende locatie bevind.")
print("Ik merk dat ik omringd ben door een prachtige, groene omgeving met hoge bomen. \nIk hoor het zachte geritsel van bladeren dat wordt veroorzaakt door de wind.")
print("Nadenkend over mijn omgeving, vroeg ik me in verwarring af, 'Waar ben ik? Wat voor plek is dit?' Het voelde vreemd en onbekend.")
print("Terwijl ik bewust ben dat dit niet mijn vertrouwde thuis, \nkon ik me ook niet herinneren waar ik wel vandaan kwam.")
print("Ik probeer mijn naam te herinneren, maar er verschijnt niets in mijn gedachten.")
print("Terwijl ik worstel om mijn vage herinneringen op te frissen, \nkomt er uiteindelijk een naam naar boven.")

def vraag_naam():
    while True:
        naam = input("Voer uw naam in: ")
        while not naam.isalpha():
            print("Ongeldige invoer. Voer alleen letters in uw naam.")
            naam = input("Voer uw naam in: ")

        bevestiging_naam = input(f"Uw naam is {naam}, klopt dit? (ja/nee): ").lower()
        while bevestiging_naam not in ["ja", "nee"]:
            print("Antwoord alstublieft met 'ja' of 'nee'.")
            bevestiging_naam = input(f"Uw naam is {naam}, klopt dit? (ja/nee): ").lower()

        if bevestiging_naam == "ja":
            return naam

naam = vraag_naam()

print(f"'{naam},' mompel ik, alsof ik het voor het eerst hoor,\nmaar het klinkt ook zo vertrouwd. ")

print("[Nieuwe informatie is toegevoegd aan uw profiel!]")

nieuwe_informatie = (f"[Naam: {naam}]")

while True:
    profiel = input("Open profiel? (ja/nee) ")
    if profiel.lower() == "ja":
        profiel_inhoud.append(f"{nieuwe_informatie}")
        break
    elif profiel.lower() == "nee":
        print("[Je hebt ervoor gekozen je profiel niet te openen. Het verhaal gaat verder.]")
        break
    else:
        print("Antwoord alstublieft met 'ja' of 'nee'.")

for extra_info in profiel_inhoud:
    print(extra_info)