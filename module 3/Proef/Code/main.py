from data import *
from functions import *

def main():
    print(PROMPT_WELKOM)

    totaal_bolletjes = 0
    totaal_hoorntjes = 0
    totaal_bakjes = 0

    while True:
        # Vraag naar het aantal bolletjes
        aantal_bolletjes = vraag_aantal_bolletjes()

        # Verwerk het aantal bolletjes
        if not antwoord_bolletjes(aantal_bolletjes):
            continue

        # Vraag of ze een hoorntje of bakje willen
        keuze = vraag_keuze_bakje_hoorntje(aantal_bolletjes)
        
        # Voeg de bestellingen toe aan de totaalsom
        if keuze == 'hoorntje':
            totaal_hoorntjes += 1
        elif keuze == 'bakje':
            totaal_bakjes += 1
        totaal_bolletjes += aantal_bolletjes

        # Vraag of ze meer willen bestellen
        if not vraag_meer_bestellen():
            break

    # Print de bon na het beëindigen van de bestelling
    druk_bonnetje_af(totaal_bolletjes, totaal_hoorntjes, totaal_bakjes)

main()