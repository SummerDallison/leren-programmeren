from data import *

# Vraag het type klant (particulier of zakelijk)
def vraag_klanttype() -> int:
    while True:
        klanttype = input(PROMPT_KLANT).strip()
        if klanttype in ["1", "2"]:
            return int(klanttype)
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

# Vraagt het aantal liters aan de zakelijke klant
def vraag_aantal_liters() -> int:
    while True:
        try:
            aantal = int(input(PROMPT_LITERS))
            if aantal > 0:
                return aantal
            print(ERROR_ONBEKEND)
        except ValueError:
            print(ERROR_ONBEKEND)

# Vraagt de smaak voor elk bolletje en houdt een teller bij voor de gekozen smaken
def vraag_smaken_bolletjes(aantal: int, smaken_teller: dict):
    for bolletje_nummer in range(1, aantal + 1):
        while True:
            smaak = input(PROMPT_SMAAK.format(bolletje_nummer=bolletje_nummer)).lower()
            if smaak in ["a", "c", "m", "v"]:
                smaken_teller[{"a": "aardbei", "c": "chocolade", "m": "munt", "v": "vanille"}[smaak]] += 1
                break
            print(ERROR_ONBEKEND)

# Vraagt de smaak voor elke liter en houdt een teller bij voor de gekozen smaken
def vraag_smaken_liters(aantal: int, smaken_teller: dict):
    for liter_nummer in range(1, aantal + 1):
        while True:
            smaak = input(PROMPT_SMAAK_LITER.format(liter_nummer=liter_nummer)).lower()
            if smaak in ["a", "c", "m", "v"]:
                smaken_teller[{"a": "aardbei", "c": "chocolade", "m": "munt", "v": "vanille"}[smaak]] += 1
                break
            print(ERROR_ONBEKEND)

# Vraagt de keuze tussen een hoorntje of een bakje
def vraag_keuze_bakje_hoorntje(aantal: int) -> str:
    while True:
        keuze = input(PROMPT_KEUZE.format(aantal=aantal)).lower()
        if keuze in KEUZE_HOORNTJE_BAKJE:
            return keuze
        print(ERROR_ONBEKEND)

# Vraagt welke topping de gebruiker wil en berekent de prijs
def vraag_topping(aantal: int, keuze: str):
    while True:
        keuze_topping = input(PROMPT_TOPPING).lower()
        if keuze_topping in ["a", "b", "c", "d"]:
            # Zet de keuze om naar een toppingnaam en bereken de prijs
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
def toon_bakje_hoorntje(aantal: int, keuze: str, topping: str):
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
def vraag_meer_bestellen() -> bool:
    while True:
        antwoord = input(PROMPT_MEER).lower()
        if antwoord in ["ja", "nee"]:
            if antwoord == "nee":
                print(AFSLUITING)
            return antwoord == "ja"
        else:
            print(ERROR_ONBEKEND)

# Print een bonnetje voor particuliere klanten
def print_bonnetje(totaal: dict):
    print(BEGIN_BONNETJE)
    for smaak, aantal in totaal["smaken"].items():
        if aantal > 0:
            prijs = aantal * BOLLETJE
            print(BON_SMAAK.format(smaak=smaak.capitalize(), aantal=aantal, BOLLETJE=BOLLETJE, prijs=prijs))
    if totaal["hoorntjes"] > 0:
        prijs_hoorntjes = totaal["hoorntjes"] * HOORNTJE
        print(BON_HOORNTJES.format(totaal_hoorntjes=totaal["hoorntjes"], HOORNTJE=HOORNTJE, prijs_hoorntjes=prijs_hoorntjes))
    if totaal["bakjes"] > 0:
        prijs_bakjes = totaal["bakjes"] * BAKJE
        print(BON_BAKJES.format(totaal_bakjes=totaal["bakjes"], BAKJE=BAKJE, prijs_bakjes=prijs_bakjes))
    if totaal["toppings"] > 0:
        print(BON_TOPPING.format(totaal_topping_prijs=totaal["toppings"]))
    totaal_prijs = (
        sum([aantal * BOLLETJE for aantal in totaal["smaken"].values()]) +
        totaal["hoorntjes"] * HOORNTJE +
        totaal["bakjes"] * BAKJE +
        totaal["toppings"]
    )
    print(BON_OPTELTEKEN)
    print(BON_TOTAAL.format(totaal_prijs=totaal_prijs))

# Print een overzichtsbonnetje met BTW voor zakelijke klanten
def print_bonnetje_zakelijk(totaal: dict):
    print(BEGIN_BONNETJE)
    totaal_prijs = 0

    for smaak, aantal in totaal["smaken"].items():
        if aantal > 0:
            prijs_inclusief_btw = aantal * LITER_PRIJS
            totaal_prijs += prijs_inclusief_btw
            print(BON_LITER.format(
                smaak=smaak.capitalize(),
                aantal=aantal,
                LITER_PRIJS=LITER_PRIJS,
                liter_prijs=prijs_inclusief_btw
            ))

    # Bereken basisprijs (exclusief BTW) en BTW-bedrag
    basis_prijs = totaal_prijs / (1 + BTW_PERCENTAGE / 100)
    btw_bedrag = totaal_prijs - basis_prijs

    print(BON_OPTELTEKEN)
    print(BON_TOTAAL.format(totaal_prijs=totaal_prijs))
    print(BON_BTW.format(BTW_PERCENTAGE=BTW_PERCENTAGE, btw_bedrag=btw_bedrag))