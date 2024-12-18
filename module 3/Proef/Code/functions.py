from data import *

def vraag_aantal_bolletjes():
    while True:
        try:
            aantal = int(input(PROMPT_BOLLETJES))
            if aantal > 0:
                return aantal
            print(ERROR_ONBEKEND)
        except ValueError:
            print(ERROR_ONBEKEND)

def vraag_smaken_bolletjes(aantal, smaken_teller):
    for x in range(1, aantal + 1):
        while True:
            smaak = input(PROMPT_SMAAK.format(X=x)).lower()
            if smaak in ["a", "c", "m", "v"]:
                smaken_teller[{"a": "aardbei", "c": "chocolade", "m": "munt", "v": "vanille"}[smaak]] += 1
                break
            print(ERROR_ONBEKEND)

def vraag_keuze_bakje_hoorntje(aantal):
    while True:
        keuze = input(PROMPT_KEUZE.format(aantal=aantal)).lower()
        if keuze in KEUZE_HOORNTJE_BAKJE:
            return keuze
        print(ERROR_ONBEKEND)

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

def toon_bakje_hoorntje(aantal, keuze, topping):
    if topping == "geen":
        print(ANTWOORD_BAKJE.format(aantal=aantal) if keuze == "bakje" else ANTWOORD_HOORNTJE_BAKJE.format(keuze=keuze, aantal=aantal))
    else:
        print(ANTWOORD_BAKJE_TOPPING.format(aantal=aantal, topping=topping) if keuze == "bakje" else ANTWOORD_HOORNTJE_TOPPING.format(keuze=keuze, aantal=aantal, topping=topping))

def vraag_meer_bestellen():
    while True:
        antwoord = input(PROMPT_MEER).lower()
        if antwoord in ["ja", "nee"]:
            print(AFSLUITING if antwoord == "nee" else "")
            return antwoord == "ja"
        print(ERROR_ONBEKEND)

def print_bonnetje(totaal):
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
    totaal_prijs = sum([aantal * BOLLETJE for aantal in totaal["smaken"].values()]) + totaal["hoorntjes"] * HOORNTJE + totaal["bakjes"] * BAKJE + totaal["toppings"]
    print(BON_OPTELTEKEN)
    print(BON_TOTAAL.format(totaal_prijs=totaal_prijs))