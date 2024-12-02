from functions import *
from data import *

def start_programma():
    print(PROMPT_WELKOM)

    while True:
        aantal_bolletjes = vraag_aantal_bolletjes()

        if 1 <= aantal_bolletjes <= 3:
            keuze = vraag_hoorntje_of_bakje()
            geef_order_bevestiging(keuze, aantal_bolletjes)

        elif 4 <= aantal_bolletjes <= 8:
            geef_bakje_met_bolletjes(aantal_bolletjes)

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