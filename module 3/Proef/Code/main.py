from data import *
from functions import *

def main():
    print(PROMPT_WELKOM)

    totaal_bolletjes = 0
    totaal_hoorntjes = 0
    totaal_bakjes = 0
    totaal_topping_prijs = 0.0
    smaken_teller = {smaak: 0 for smaak in KEUZE_SMAAK_BOLLETJE}

    while True:
        # Vraag naar het aantal bolletjes
        aantal_bolletjes = vraag_aantal_bolletjes()

        # Controleer of het aantal bolletjes boven de 8 is
        if aantal_bolletjes > 8:
            print(ERROR_BAKKEN)
            continue  # Ga terug naar het begin van de lus

        # Vraag de smaak voor elk bolletje
        vraag_smaken_bolletjes(aantal_bolletjes, smaken_teller)

        # Verwerk het aantal bolletjes en de keuze voor hoorntje of bakje
        keuze = antwoord_bolletjes(aantal_bolletjes)
        if not keuze:
            continue

        # Vraag naar topping en verwerk de prijs
        topping, topping_prijs = vraag_topping(aantal_bolletjes, keuze)
        totaal_topping_prijs += topping_prijs

        antwoord_bolletjes(aantal_bolletjes, topping)

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
            print_bonnetje(totaal_bolletjes, totaal_hoorntjes, totaal_bakjes, smaken_teller, totaal_topping_prijs)
            break

main()