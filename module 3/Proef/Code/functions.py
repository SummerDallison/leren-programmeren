from data import *

# Vraag het type klant (particulier of zakelijk)
def vraag_klanttype() -> int:
    while True:
        klanttype = input(PROMPT_KLANT).strip()
        if klanttype in ["1", "2"]:
            return int(klanttype)
        print(ERROR_ONBEKEND)

# Vraagt het aantal bolletjes/liters aan de gebruiker
def vraag_aantal(prompt: str) -> int:
    while True:
        try:
            aantal = int(input(prompt))
            if aantal > 0:
                return aantal
            print(ERROR_ONBEKEND)
        except ValueError:
            print(ERROR_ONBEKEND)

# Vraagt de smaak voor elk bolletje en houdt een teller bij voor de gekozen smaken
def vraag_smaken(aantal: int, smaken_teller: dict, prompt: str):
    for nummer in range(1, aantal + 1):
        while True:
            smaak = input(prompt.format(nummer=nummer)).lower()
            if smaak in ["a", "c", "v"]:
                smaken_teller[{"a": "aardbei", "c": "chocolade", "v": "vanille"}[smaak]] += 1
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

def print_bonnetje(totaal: dict, klanttype: int):
    print(BEGIN_BONNETJE)
    totaal_prijs = 0

    # Bon voor particuliere klanten
    if klanttype == 1:
        for smaak, aantal in totaal["smaken"].items():
            if aantal > 0:
                prijs = aantal * BOLLETJE
                totaal_prijs += prijs
                print(BON_SMAAK.format(smaak=smaak.capitalize(), aantal=aantal, BOLLETJE=BOLLETJE, prijs=prijs))
        
        if totaal["hoorntjes"] > 0:
            prijs_hoorntjes = totaal["hoorntjes"] * HOORNTJE
            totaal_prijs += prijs_hoorntjes
            print(BON_HOORNTJES.format(totaal_hoorntjes=totaal["hoorntjes"], HOORNTJE=HOORNTJE, prijs_hoorntjes=prijs_hoorntjes))

        if totaal["bakjes"] > 0:
            prijs_bakjes = totaal["bakjes"] * BAKJE
            totaal_prijs += prijs_bakjes
            print(BON_BAKJES.format(totaal_bakjes=totaal["bakjes"], BAKJE=BAKJE, prijs_bakjes=prijs_bakjes))

        if totaal["toppings"] > 0:
            print(BON_TOPPING.format(totaal_topping_prijs=totaal["toppings"]))

    # Bon voor zakelijke klanten
    elif klanttype == 2:
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

    # Bereken en toon totaalbedrag
    print(BON_OPTELTEKEN)

    if klanttype == 1:
        print(BON_TOTAAL.format(totaal_prijs=totaal_prijs))
    elif klanttype == 2:
        # Voor zakelijke klanten wordt BTW berekend
        basis_prijs = totaal_prijs / (1 + BTW_PERCENTAGE / 100)
        btw_bedrag = totaal_prijs - basis_prijs
        print(BON_TOTAAL.format(totaal_prijs=totaal_prijs))
        print(BON_BTW.format(BTW_PERCENTAGE=BTW_PERCENTAGE, btw_bedrag=btw_bedrag))