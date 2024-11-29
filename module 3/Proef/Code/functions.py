from data import *

def vraag_bolletjes():
    while True:
        try:
            aantal_bolletjes = int(input(PROMPT_BOLLETJES))
            return aantal_bolletjes
        except ValueError:
            print(ERROR_ONBEKEND)

def vraag_keuze(aantal):
    while True:
        keuze = input(PROMPT_KEUZE.format(aantal=aantal)).lower()
        if keuze in KEUZE_HOORNTJE_BAKJE:
            print(ANTWOORD_HOORNTJE_BAKJE.format(keuze=keuze, aantal=aantal))
            return keuze
        else:
            print(ERROR_ONBEKEND)

def check_aantal_bolletjes(aantal):
    if 1 <= aantal <= 3:
        return True
    elif 4 <= aantal <= 8:
        print(ANTWOORD_BAKJE.format(aantal=aantal))
        return False
    elif aantal > 8:
        print(ERROR_BAKKEN)
        return False
    else:
        print(ERROR_ONBEKEND)
        return False

def vraag_meer_bestellen():
    while True:
        antwoord = input(PROMPT_MEER).lower()
        if antwoord == 'ja' or antwoord == 'nee':
            return antwoord
        else:
            print(ERROR_ONBEKEND)