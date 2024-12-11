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

        # Verwerk het aantal bolletjes en de keuze voor hoorntje of bakje
        keuze = antwoord_bolletjes(aantal_bolletjes)
        if not keuze:
            continue  

        # Tel de bestellingen op
        totaal_bolletjes += aantal_bolletjes

        # Verhoog de juiste teller afhankelijk van de keuze
        if keuze == "hoorntje":
            totaal_hoorntjes += 1
        elif keuze == "bakje":
            totaal_bakjes += 1

        # Vraag of ze meer willen bestellen
        if not vraag_meer_bestellen():
            # Toon het bonnetje als ze klaar zijn
            print_bonnetje(totaal_bolletjes, totaal_hoorntjes, totaal_bakjes)
            break

main()