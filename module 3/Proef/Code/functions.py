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

def vraag_topping(aantal_bolletjes, keuze_bakje_hoorntje):
    while True:
        topping_keuze = input(PROMPT_TOPPING).lower()
        if topping_keuze in ['a', 'b', 'c', 'd']:
            topping = {"a": "geen", "b": "slagroom", "c": "sprinkels", "d": "caramel saus"}[topping_keuze]
            
            if topping == "geen":
                return topping, 0.0
            elif topping == "sprinkels":
                return topping, aantal_bolletjes * TOPPING_PRIJZEN[topping]
            elif topping == "caramel saus":
                # Haal de prijs op afhankelijk van bakje of hoorntje
                return topping, TOPPING_PRIJZEN[topping][keuze_bakje_hoorntje]
            else:
                return topping, TOPPING_PRIJZEN[topping]
        else:
            print(ERROR_ONBEKEND)

def antwoord_bolletjes(aantal_bolletjes, topping=None):
    if 1 <= aantal_bolletjes <= 3:
        keuze = vraag_keuze_bakje_hoorntje(aantal_bolletjes)
        if topping and topping != "geen":
            print(ANTWOORD_HOORNTJE_TOPPING.format(keuze=keuze, aantal=aantal_bolletjes, topping=topping))
        else:
            print(ANTWOORD_HOORNTJE_BAKJE.format(keuze=keuze, aantal=aantal_bolletjes))
        return keuze 
    elif 4 <= aantal_bolletjes <= 8:
        if topping and topping != "geen":
            print(ANTWOORD_BAKJE_TOPPING.format(aantal=aantal_bolletjes, topping=topping))
        else:
            print(ANTWOORD_BAKJE.format(aantal=aantal_bolletjes))
        return "bakje"
    elif aantal_bolletjes > 8:
        print(ERROR_BAKKEN)
        return False
    else:
        print(ERROR_ONBEKEND)
        return False
    
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
    
def toon_bakje_hoorntje(aantal_bolletjes, keuze, topping):
    if topping != "geen":
        if keuze == "bakje":
            print(ANTWOORD_BAKJE_TOPPING.format(aantal=aantal_bolletjes, topping=topping))
        elif keuze == "hoorntje":
            print(ANTWOORD_HOORNTJE_TOPPING.format(keuze=keuze, aantal=aantal_bolletjes, topping=topping))
    else:
        if keuze == "bakje":
            print(ANTWOORD_BAKJE.format(aantal=aantal_bolletjes))
        elif keuze == "hoorntje":
            print(ANTWOORD_HOORNTJE_BAKJE.format(keuze=keuze, aantal=aantal_bolletjes))
    
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

def print_bonnetje(totaal_bolletjes, totaal_hoorntjes, totaal_bakjes, smaken_teller, totaal_topping_prijs):
    print(BEGIN_BONNETJE)

    for smaak, aantal in smaken_teller.items():
        if aantal > 0:
            prijs = aantal * BOLLETJE
            print(BON_SMAAK.format(smaak=smaak.capitalize(), aantal=aantal, BOLLETJE=BOLLETJE, prijs=prijs))

    prijs_hoorntjes = totaal_hoorntjes * HOORNTJE
    prijs_bakjes = totaal_bakjes * BAKJE

    if totaal_hoorntjes > 0:
        print(BON_HOORNTJES.format(totaal_hoorntjes=totaal_hoorntjes, HOORNTJE=HOORNTJE, prijs_hoorntjes=prijs_hoorntjes))
    if totaal_bakjes > 0:
        print(BON_BAKJES.format(totaal_bakjes=totaal_bakjes, BAKJE=BAKJE, prijs_bakjes=prijs_bakjes))

    if totaal_topping_prijs > 0:
        print(BON_TOPPING.format(totaal_topping_prijs=totaal_topping_prijs))

    totaal_prijs = sum(aantal * BOLLETJE for aantal in smaken_teller.values()) + prijs_hoorntjes + prijs_bakjes + totaal_topping_prijs
    print(BON_OPTELTEKEN)
    print(BON_TOTAAL.format(totaal_prijs=totaal_prijs))