from data import *

def vraag_aantal_bolletjes():
    while True:
        try:
            aantal_bolletjes = int(input(PROMPT_BOLLETJES))
            return aantal_bolletjes
        except ValueError:
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
    elif 4 <= aantal_bolletjes <= 8:
        print(ANTWOORD_BAKJE.format(aantal=aantal_bolletjes))
    elif aantal_bolletjes > 8:
        print(ERROR_BAKKEN)
        return False # Geef False terug om aan te geven dat we moeten herhalen
    else:
        print(ERROR_ONBEKEND)
        return False
    return True # Geef True terug als alles goed is gegaan

def vraag_meer_bestellen():
    while True:
        meer_bestellen = input(PROMPT_MEER).lower()
        if meer_bestellen == "ja":
            return True # Geef True terug om het proces opnieuw te starten
        elif meer_bestellen == "nee":
            print(AFSLUITING)
            return False # Geef False terug om het programma te beëindigen
        else:
            print(ERROR_ONBEKEND)

from data import *

def druk_bonnetje_af(totaal_bolletjes, totaal_hoorntjes, totaal_bakjes):
    prijs_bolletjes = totaal_bolletjes * BOLLETJE
    prijs_hoorntjes = totaal_hoorntjes * HOORNTJE
    prijs_bakjes = totaal_bakjes * BAKJE
    totaal_prijs = prijs_bolletjes + prijs_hoorntjes + prijs_bakjes

    print(BEGIN_BONNETJE)

    if totaal_bolletjes > 0:
        print(BON_BOLLETJES.format(totaal_bolletjes=totaal_bolletjes, prijs_bolletjes=prijs_bolletjes))

    if totaal_hoorntjes > 0:
        print(BON_HOORNTJES.format(totaal_hoorntjes=totaal_hoorntjes, prijs_hoorntjes=prijs_hoorntjes))

    if totaal_bakjes > 0:
        print(BON_BAKJES.format(totaal_bakjes=totaal_bakjes, prijs_bakjes=prijs_bakjes))

    print(BON_OPTELTEKEN)
    print(BON_TOTAAL.format(totaal_prijs=totaal_prijs))
    print(AFSLUITING)