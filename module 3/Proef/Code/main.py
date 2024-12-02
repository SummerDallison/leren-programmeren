from functions import *
from data import *

def main():
    print(PROMPT_WELKOM)

    while True:
        aantal_bolletjes = krijg_aantal_bolletjes()
        while not verwerk_aantal_bolletjes(aantal_bolletjes):
            aantal_bolletjes = krijg_aantal_bolletjes()  # Vraag opnieuw bij te groot aantal

        if aantal_bolletjes:  # Alleen verder als stap 2 nodig is
            vraag_keuze(aantal_bolletjes)
        
        if not vraag_meer_bestellen():
            break

main()