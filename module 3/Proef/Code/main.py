from functions import *
from data import *

def main():
    print(PROMPT_WELKOM)

    while True:
        aantal_bolletjes = krijg_aantal_bolletjes()
        if aantal_bolletjes:
            resultaat = verwerk_aantal_bolletjes(aantal_bolletjes)
            if resultaat:  # Alleen verder als stap 2 nodig is
                vraag_keuze(resultaat)
        if not vraag_meer_bestellen():
            break

main()