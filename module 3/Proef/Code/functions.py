from data import *

def vraag_aantal_bolletjes():
    while True:
        try:
            aantal_bolletjes = int(input(PROMPT_BOLLETJES))
            if aantal_bolletjes > 0:
                return aantal_bolletjes
            else:
                print(ERROR_ONBEKEND)
        except ValueError:
            print(ERROR_ONBEKEND)

def vraag_smaken_bolletjes(aantal_bolletjes, smaken_teller):
    for x in range(1, aantal_bolletjes + 1):
        while True:
            smaak = input(PROMPT_SMAAK.format(X=x)).lower()
            if smaak in ['a', 'c', 'm', 'v']:
                smaak_naam = {"a": "aardbei", "c": "chocolade", "m": "munt", "v": "vanille"}[smaak]
                smaken_teller[smaak_naam] += 1
                break
            else:
                print(ERROR_ONBEKEND)

def vraag_keuze_bakje_hoorntje(aantal_bolletjes):
    while True:
        keuze = input(PROMPT_KEUZE.format(aantal=aantal_bolletjes)).lower()
        if keuze in KEUZE_HOORNTJE_BAKJE:
            return keuze
        else:
            print(ERROR_ONBEKEND)

def vraag_topping(keuze, aantal_bolletjes):
    while True:
        topping_keuze = input(PROMPT_TOPPING).lower()
        if topping_keuze in ["a", "b", "c", "d"]:
            if topping_keuze == "a":
                return "geen", 0.0
            elif topping_keuze == "b":
                return "slagroom", TOPPING_PRIJZEN["slagroom"]
            elif topping_keuze == "c":
                return "sprinkels", aantal_bolletjes * TOPPING_PRIJZEN["sprinkels"]
            elif topping_keuze == "d":
                prijs = TOPPING_PRIJZEN["caramel saus"][keuze]
                return "caramel saus", prijs
        else:
            print(ERROR_ONBEKEND)

def antwoord_bolletjes(aantal_bolletjes, keuze, topping):
    if 1 <= aantal_bolletjes <= 3:
        if topping[0] == "geen":
            print(ANTWOORD_HOORNTJE_BAKJE.format(keuze=keuze, aantal=aantal_bolletjes))
        else:
            print(ANTWOORD_HOORNTJE_TOPPING.format(keuze=keuze, aantal=aantal_bolletjes, topping=topping[0]))
    elif 4 <= aantal_bolletjes <= 8:
        if topping[0] == "geen":
            print(ANTWOORD_BAKJE.format(aantal=aantal_bolletjes))
        else:
            print(ANTWOORD_BAKJE_TOPPING.format(aantal=aantal_bolletjes, topping=topping[0]))

def vraag_meer_bestellen():
    while True:
        meer_bestellen = input(PROMPT_MEER).lower()
        if meer_bestellen == "ja":
            return True 
        elif meer_bestellen == "nee":
            print(AFSLUITING)
            return False
        else:
            print(ERROR_ONBEKEND)

def print_bonnetje(totaal_bolletjes, totaal_hoorntjes, totaal_bakjes, smaken_teller, totaal_topping):
    print(BEGIN_BONNETJE)

    prijs_bolletjes = totaal_bolletjes * BOLLETJE
    prijs_hoorntjes = totaal_hoorntjes * HOORNTJE
    prijs_bakjes = totaal_bakjes * BAKJE

    if totaal_bolletjes > 0:
        print(BON_BOLLETJES.format(totaal_bolletjes=totaal_bolletjes, BOLLETJE=BOLLETJE, prijs_bolletjes=prijs_bolletjes))
    if totaal_hoorntjes > 0:
        print(BON_HOORNTJES.format(totaal_hoorntjes=totaal_hoorntjes, HOORNTJE=HOORNTJE, prijs_hoorntjes=prijs_hoorntjes))
    if totaal_bakjes > 0:
        print(BON_BAKJES.format(totaal_bakjes=totaal_bakjes, BAKJE=BAKJE, prijs_bakjes=prijs_bakjes))
    if totaal_topping > 0:
        print(BON_TOPPINGS.format(prijs_toppings=totaal_topping))

    totaal_prijs = prijs_bolletjes + prijs_hoorntjes + prijs_bakjes + totaal_topping
    print(BON_OPTELTEKEN)
    print(BON_TOTAAL.format(totaal_prijs=totaal_prijs))

    print(AFSLUITING)