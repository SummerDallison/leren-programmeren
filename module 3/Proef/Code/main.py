from data import *
from functions import *

def main():
    print(PROMPT_WELKOM)

    totaal = {
        "bolletjes": 0,
        "hoorntjes": 0,
        "bakjes": 0,
        "toppings": 0.0,
        "smaken": {smaak: 0 for smaak in KEUZE_SMAAK_BOLLETJE}
    }

    while True:
        # Vraag aantal bolletjes
        aantal_bolletjes = vraag_aantal_bolletjes()
        if aantal_bolletjes > 8:
            print(ERROR_BAKKEN)
            continue
        
        # Vraag smaken en update smaken teller
        vraag_smaken_bolletjes(aantal_bolletjes, totaal["smaken"])

        # Bepaal bakje of hoorntje
        keuze = "bakje" if aantal_bolletjes > 3 else vraag_keuze_bakje_hoorntje(aantal_bolletjes)
        if keuze == "hoorntje":
            totaal["hoorntjes"] += 1
        else:
            totaal["bakjes"] += 1

        # Vraag topping
        topping, topping_prijs = vraag_topping(aantal_bolletjes, keuze)
        totaal["toppings"] += topping_prijs

        # Toon keuze
        toon_bakje_hoorntje(aantal_bolletjes, keuze, topping)

        # Totaal aantal bolletjes
        totaal["bolletjes"] += aantal_bolletjes

        # Check of er meer besteld moet worden
        if not vraag_meer_bestellen():
            print_bonnetje(totaal)
            break

main()