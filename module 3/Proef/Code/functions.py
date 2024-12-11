from data import *

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

def antwoord_bolletjes(aantal_bolletjes):
    if 1 <= aantal_bolletjes <= 3:
        keuze = vraag_keuze_bakje_hoorntje(aantal_bolletjes)
        print(ANTWOORD_HOORNTJE_BAKJE.format(keuze=keuze, aantal=aantal_bolletjes))
        return keuze 
    elif 4 <= aantal_bolletjes <= 8:
        print(ANTWOORD_BAKJE.format(aantal=aantal_bolletjes))
        return "bakje"
    elif aantal_bolletjes > 8:
        return False  # Geen verdere acties als het aantal te groot is
    else:
        print(ERROR_ONBEKEND)
        return False

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

def print_bonnetje(totaal_bolletjes, totaal_hoorntjes, totaal_bakjes, smaken_teller):
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

    totaal_prijs = sum(aantal * BOLLETJE for aantal in smaken_teller.values()) + prijs_hoorntjes + prijs_bakjes
    print(BON_OPTELTEKEN)
    print(BON_TOTAAL.format(totaal_prijs=totaal_prijs))

    print(AFSLUITING)