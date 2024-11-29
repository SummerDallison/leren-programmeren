from data import *
from functions import *

def start_programma():
    print(PROMPT_WELKOM)

    while True:
        aantal_bolletjes = vraag_aantal_bolletjes()

        if aantal_bolletjes is None:
            continue

        if 1 <= aantal_bolletjes <= 3:
            keuze = vraag_aantal_bolletjes(aantal_bolletjes)
            print(ANTWOORD_HOORNTJE_BAKJE.format(aantal=aantal_bolletjes, keuze=keuze))
        elif 4 <= aantal_bolletjes <= 8:
            print(ANTWOORD_BAKJE.format(aantal=aantal_bolletjes))
        elif aantal_bolletjes > 8:
            print(ERROR_BAKKEN)
            continue
        else:
            print(ERROR_ONBEKEND)
            continue

        if not vraag_meer_bestellen():
            print(AFSLUITING)
            break

start_programma()