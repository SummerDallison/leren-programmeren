from functions import *
from data import *

def main():
    print(PROMPT_WELKOM)

    while True:
        aantal_bolletjes = krijg_aantal_bolletjes()
        if aantal_bolletjes:  # Gaat verder alleen bij geldige invoer (niet None of False)
            if not verwerk_aantal_bolletjes(aantal_bolletjes):
                continue  # Foutmelding bij >8 bolletjes; ga terug naar de vraag
            # Voor 4-8 bolletjes wordt al direct het bericht getoond en niets gedaan

            if 1 <= aantal_bolletjes <= 3:
                vraag_keuze(aantal_bolletjes)
        
        if not vraag_meer_bestellen():
            break

main()