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
        return False
    else:
        print(ERROR_ONBEKEND)
        return False
    return True

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