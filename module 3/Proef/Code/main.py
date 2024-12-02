from functions import *
from data import *

def main():
    print(PROMPT_WELKOM)

    while True:
        aantal_bolletjes = krijg_aantal_bolletjes()  # Vraag altijd eerst het aantal bolletjes
        
        # Verwerk het aantal bolletjes en bepaal de flow
        if 1 <= aantal_bolletjes <= 3:
            vraag_keuze(aantal_bolletjes)  # Alleen voor 1-3 bolletjes
        elif 4 <= aantal_bolletjes <= 8:
            print(ANTWOORD_BAKJE.format(aantal=aantal_bolletjes))  # Direct naar bakje-uitvoer
        else:
            continue  # Meer dan 8 bolletjes: terug naar bolletjesvraag
        
        # Vraag na een succesvolle bestelling of de klant meer wil bestellen
        if not vraag_meer_bestellen():
            break

main()