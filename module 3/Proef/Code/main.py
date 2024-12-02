from functions import *
from data import *

def main():
    print(PROMPT_WELKOM)

    while True:
        aantal_bolletjes = krijg_aantal_bolletjes()
        aantal_verwerkt = verwerk_aantal_bolletjes(aantal_bolletjes)

        # Alleen verdergaan naar stap 2 als verwerk_aantal_bolletjes geen None teruggeeft
        if aantal_verwerkt:
            vraag_keuze(aantal_verwerkt)
        
        # Vraag alleen na afhandeling of ze meer willen
        if not vraag_meer_bestellen():
            break

main()