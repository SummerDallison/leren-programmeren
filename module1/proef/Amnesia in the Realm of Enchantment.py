print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">          Amnesia in the Realm of Enchantment          >")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

inventaris = []
companions = []
profiel_inhoud = []

print("Ik word langzaam wakker en knijp mijn ogen samen in een poging om te wennen aan het verblindende zonlicht dat mijn zicht overweldigt.")
print("Ik kijk verward om me heen en besef dat ik op een onbekende locatie bevind.")
print("Ik merk dat ik omringd ben door een prachtige, groene omgeving met hoge bomen. Ik hoor het zachte geritsel van bladeren dat wordt veroorzaakt door de wind.")
print("Nadenkend over mijn omgeving, vroeg ik me in verwarring af, 'Waar ben ik? Wat voor plek is dit?' Het voelde vreemd en onbekend.")
print("Terwijl ik bewust ben dat dit niet mijn vertrouwde thuis, kon ik me ook niet herinneren waar ik wel vandaan kwam.")
print("Ik probeer mijn naam te herinneren, maar er verschijnt niets in mijn gedachten.")
print("Terwijl ik worstel om mijn vage herinneringen op te frissen, komt er uiteindelijk een naam naar boven.")

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

print(f"'{naam},' mompel ik, alsof ik het voor het eerst hoor, maar het klinkt ook zo vertrouwd. ")

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

print("Ik neem het besluit om verder te lopen, vastbesloten om de mysteries van deze onbekende plek te ontrafelen.")
print("Ik ontdek een oude bibliotheek tussen de bomen. De deuren kraken en overal liggen stoffige boeken.")

while True:
    keuze_bibliotheek = input("Moet ik de tijd nemen om de boeken te bekijken, of snel doorgaan met mijn reis?\n(tijd/doorgaan): ")

    if keuze_bibliotheek.lower() == "tijd":
        print("[Je besloot om de tijd te nemen om de boeken te bekijken.]")
        print("Ik werp een blik op de boekenplanken en besluit enkele boeken op te pikken om te verkennen.")
        
        print("Terwijl ik tussen de verweerde boekenplanken speur, stuit ik op verborgen compartimenten met twee magische artefacten.")
        print("De eerste artefact is een zwart kristal met mysterieuze inscripties.")
        print("De tweede artefact is een gouden amulet met een glinsterende edelsteen.")

        while True:
            pick_artefacts = input("Wil je de magische artefacten oppakken? (ja/nee): ")

            if pick_artefacts.lower() == "ja":
                while True:
                    beide_artefacten = input("Wil je beide artefacten oppakken? (ja/nee): ")
            
                    if beide_artefacten.lower() == "ja":
                        print("[Zwart kristal toegevoegd aan inventaris!]")
                        inventaris.append("Zwarte artefact")
                        print("[Gouden amulet toegevoegd aan inventaris!]")
                        inventaris.append("Gouden artefact")
            
                    elif beide_artefacten.lower() == "nee":
                        while True:
                            welk_artefact = input("Welke artefact wil je oppakken? (zwart/goud): ")
                            if welk_artefact.lower() == "zwart":
                                print("[Zwarte artefact toegevoegd aan inventaris!]")
                                inventaris.append("Zwarte artefact")
                            elif welk_artefact.lower() == "goud":
                                print("[Gouden artefact toegevoegd aan inventaris!]")
                                inventaris.append("Gouden artefact")
                            else:
                                print("Antwoord alstublieft met 'zwart' of 'goud'.")
                    else:
                        print("Antwoord alstublieft met 'ja' of 'nee'.")

            elif pick_artefacts.lower() == "nee":
                print("[Je besluit om de magische artefacten met rust te laten.]")
            else:
                print("Antwoord alstublieft met 'ja' of 'nee'.")

    elif keuze_bibliotheek.lower() == "doorgaan":
        print("[Je besloot om snel door te gaan met jouw reis.]")
        print("Mijn stappen leiden me weg van de bibliotheek, op zoek naar onontdekte geheimen in dit magische wereld.")

        print("Nadat ik een tijdje door het bos heb gelopen, ontdek ik een schattig dorpje tussen de bomen.")
        print("Kleine huisjes met mooie decoraties trekken mijn aandacht, en het geluid van hamers en smeedwerk komt naar voren.")
        print("En zonder enige aarzeling besluit ik mijn weg naar het dorpje te vervolgen.")
        print("Terwijl ik verder door het dorp loop, begin ik steeds meer op te merken.")
        print("De ambachtelijke winkeltjes zitten propvol met prachtig smeedwerk, en de geur van gesmolten metaal zweeft in de lucht.")
        print("Terwijl ik om me heen kijk, zie ik mensen van een wat kleinere gestalte, stevig gebouwd en duidelijk bedreven in hun ambacht.")
        print("Langzaam dringt het tot me door: dit is geen gewoon dorp; ik ben te midden van dwergen.") 
        print("Een golf van zowel verrassing als nieuwsgierigheid spoelt over me heen.")

        print("Ik besluit  een van de ambachtelijke winkeltjes binnen te gaan.") 
        print("Het is gevuld met prachtige smeedkunst en unieke voorwerpen.")
        print("")

    else:
        print("Antwoord alstublieft met 'tijd' of 'doorgaan'.")