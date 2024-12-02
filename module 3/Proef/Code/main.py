from functions import *
from data import *

def start_programma():
    print(PROMPT_WELKOM)
    
    while True:
        aantal_bolletjes = None
        
        # Stap 1: Vraag het aantal bolletjes
        while aantal_bolletjes is None or not is_valid_aantal_bolletjes(aantal_bolletjes):
            aantal_bolletjes = vraag_aantal_bolletjes()

            if aantal_bolletjes is None or aantal_bolletjes < 1:
                print(ERROR_ONBEKEND)
            elif aantal_bolletjes > 8:
                print(ERROR_BAKKEN)
            elif 4 <= aantal_bolletjes <= 8:
                print(ANTWOORD_BAKJE.format(aantal=aantal_bolletjes))
                continue

        # Stap 2: Vraag voor hoorntje of bakje
        keuze = None
        while keuze is None:
            keuze = vraag_bakje_of_hoorntje(aantal_bolletjes)

        # Stap 3: Serveergroet
        print(ANTWOORD_HOORNTJE_BAKJE.format(keuze=keuze, aantal=aantal_bolletjes))

        # Vraag of de klant nog meer wil bestellen
        meer_bestellen = input(PROMPT_MEER).lower()
        if meer_bestellen != "ja":
            print(AFSLUITING)
            break

start_programma()