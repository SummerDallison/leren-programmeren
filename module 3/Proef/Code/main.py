from data import *
from functions import *

def main():
    print(PROMPT_WELKOM)

    totaal_bolletjes = 0
    totaal_hoorntjes = 0
    totaal_bakjes = 0
    totaal_topping = 0.0
    smaken_teller = {smaak: 0 for smaak in KEUZE_SMAAK_BOLLETJE}

    while True:
        # Vraag naar het aantal bolletjes
        aantal_bolletjes = vraag_aantal_bolletjes()

        if aantal_bolletjes > 8:
            print(ERROR_BAKKEN)
            continue

        # Vraag de smaak voor elk bolletje
        vraag_smaken_bolletjes(aantal_bolletjes, smaken_teller)

        # Vraag de keuze voor hoorntje of bakje
        keuze = vraag_keuze_bakje_hoorntje(aantal_bolletjes)

        # Vraag de topping
        topping = vraag_topping(keuze, aantal_bolletjes)
        totaal_topping += topping[1]

        # Verwerk de bestelling
        antwoord_bolletjes(aantal_bolletjes, keuze, topping)

        totaal_bolletjes += aantal_bolletjes
        if keuze == "hoorntje":
            totaal_hoorntjes += 1
        elif keuze == "bakje":
            totaal_bakjes += 1

        # Vraag of ze meer willen bestellen
        if not vraag_meer_bestellen():
            print_bonnetje(totaal_bolletjes, totaal_hoorntjes, totaal_bakjes, smaken_teller, totaal_topping)
            break

main()