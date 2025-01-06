from data import *

# Vraag klanttype
def vraag_klanttype() -> str:
    while True:
        klanttype = input(PROMPT_KLANT).strip()
        if klanttype in ["1", "2"]:
            return klanttype
        print(ERROR_ONBEKEND)

# Vraagt het aantal bolletjes aan de gebruiker
def vraag_aantal_bolletjes() -> int:
    while True:
        try:
            aantal = int(input(PROMPT_BOLLETJES))
            if aantal > 0:
                return aantal
            print(ERROR_ONBEKEND)
        except ValueError:
            print(ERROR_ONBEKEND)

# Vraag aantal liters voor zakelijke klant
def vraag_aantal_liters() -> int:
    while True:
        try:
            aantal = int(input(PROMPT_LITERS))
            if aantal > 0:
                return aantal
            print(ERROR_ONBEKEND)
        except ValueError:
            print(ERROR_ONBEKEND)

# Vraag smaken voor bolletjes of liters
def vraag_smaken_bolletjes(aantal: int, smaken_teller: dict):
    for nummer in range(1, aantal + 1):
        while True:
            smaak = input(PROMPT_SMAAK.format(bolletje_nummer=nummer)).lower()
            if smaak in ["a", "c", "m", "v"]:
                gekozen_smaak = {"a": "aardbei", "c": "chocolade", "m": "munt", "v": "vanille"}[smaak]
                smaken_teller[gekozen_smaak] += 1
                break
            print(ERROR_ONBEKEND)

# Vraag smaken voor zakelijke bestellingen
def vraag_smaken(aantal: int, item: str) -> str:
    while True:
        smaak = input(f"Welke smaak wilt u voor {item}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ").lower()
        if smaak in ["a", "c", "m", "v"]:
            gekozen_smaak = {"a": "aardbei", "c": "chocolade", "m": "munt", "v": "vanille"}[smaak]
            return gekozen_smaak
        print(ERROR_ONBEKEND)

# Vraagt de keuze tussen een hoorntje of een bakje
def vraag_keuze_bakje_hoorntje(aantal: int) -> str:
    while True:
        keuze = input(PROMPT_KEUZE.format(aantal=aantal)).lower()
        if keuze in KEUZE_HOORNTJE_BAKJE:
            return keuze
        print(ERROR_ONBEKEND)

# Vraagt welke topping de gebruiker wil en berekent de prijs
def vraag_topping(aantal, keuze):
    while True:
        keuze_topping = input(PROMPT_TOPPING).lower()
        if keuze_topping in ["a", "b", "c", "d"]:
            topping = {"a": "geen", "b": "slagroom", "c": "sprinkels", "d": "caramel saus"}[keuze_topping]
            prijs = 0.0
            if topping == "sprinkels":
                prijs = aantal * TOPPING_PRIJZEN[topping]
            elif topping == "caramel saus":
                prijs = TOPPING_PRIJZEN[topping][keuze]
            elif topping != "geen":
                prijs = TOPPING_PRIJZEN[topping]
            return topping, prijs
        print(ERROR_ONBEKEND)

# Toont aantal bolletjes, de keuze van bakje of hoorntje en de topping
def toon_bakje_hoorntje(aantal, keuze, topping):
    if topping == "geen":
        if keuze == "bakje":
            print(ANTWOORD_BAKJE.format(aantal=aantal))
        else:
            print(ANTWOORD_HOORNTJE_BAKJE.format(keuze=keuze, aantal=aantal))
    else:
        if keuze == "bakje":
            print(ANTWOORD_BAKJE_TOPPING.format(aantal=aantal, topping=topping))
        else:
            print(ANTWOORD_HOORNTJE_TOPPING.format(keuze=keuze, aantal=aantal, topping=topping))

# Vraagt of de gebruiker meer wil bestellen
def vraag_meer_bestellen():
    while True:
        antwoord = input(PROMPT_MEER).lower()
        if antwoord in ["ja", "nee"]:
            if antwoord == "nee":
                print(AFSLUITING)
            return antwoord == "ja"
        else:
            print(ERROR_ONBEKEND)

# Print een overzichtsbonnetje met de totaalprijs en specificaties
def print_bonnetje(totaal, klanttype="1"):
    print(BEGIN_BONNETJE)
    for smaak, aantal in totaal["smaken"].items():
        if aantal > 0:
            prijs = aantal * BOLLETJE
            print(BON_SMAAK.format(smaak=smaak.capitalize(), aantal=aantal, BOLLETJE=BOLLETJE, prijs=prijs))
    if totaal["hoorntjes"] > 0:
        prijs = totaal["hoorntjes"] * HOORNTJE
        print(BON_HOORNTJES.format(totaal_hoorntjes=totaal["hoorntjes"], HOORNTJE=HOORNTJE, prijs_hoorntjes=prijs))
    if totaal["bakjes"] > 0:
        prijs = totaal["bakjes"] * BAKJE
        print(BON_BAKJES.format(totaal_bakjes=totaal["bakjes"], BAKJE=BAKJE, prijs_bakjes=prijs))
    if totaal["toppings"] > 0:
        print(BON_TOPPING.format(totaal_topping_prijs=totaal["toppings"]))
    if klanttype == "2":
        totaal_prijs = totaal["liter"] * LITER
        print(BON_OPTELTEKEN)
        print(BON_TOTAAL.format(totaal_prijs=totaal_prijs))
        btw_bedrag = totaal_prijs * BTW_PERCENTAGE
        print(BON_BTW.format(btw_bedrag=btw_bedrag))
    else:
        totaal_prijs = sum([aantal * BOLLETJE for aantal in totaal["smaken"].values()]) + totaal["hoorntjes"] * HOORNTJE + totaal["bakjes"] * BAKJE + totaal["toppings"]
        print(BON_OPTELTEKEN)
        print(BON_TOTAAL.format(totaal_prijs=totaal_prijs))