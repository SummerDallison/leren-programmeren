from data import *
from functions import *

def main():
    print(PROMPT_WELKOM)

    klanttype = vraag_klanttype()
    totaal = TOTAAL.copy()

    if klanttype == 1:  # Particuliere klant
        while True:
            aantal_bolletjes = vraag_aantal(PROMPT_BOLLETJES)
            if aantal_bolletjes > 8:
                print(ERROR_BAKKEN)
                continue
            
            vraag_smaken(aantal_bolletjes, totaal["smaken"], PROMPT_SMAAK_BOLLETJE)

            if aantal_bolletjes > 3:
                keuze = "bakje"
            else:
                keuze = vraag_keuze_bakje_hoorntje(aantal_bolletjes)

            if keuze == "hoorntje":
                totaal["hoorntjes"] += 1
            else:
                totaal["bakjes"] += 1

            topping, topping_prijs = vraag_topping(aantal_bolletjes, keuze)
            totaal["toppings"] += topping_prijs

            toon_bakje_hoorntje(aantal_bolletjes, keuze, topping)

            totaal["bolletjes"] += aantal_bolletjes

            if not vraag_meer_bestellen():
                print_bonnetje(totaal)
                break
    else:  # Zakelijke klant
        aantal_liters = vraag_aantal(PROMPT_LITERS)
        vraag_smaken(aantal_liters, totaal["smaken"], PROMPT_SMAAK_LITER)
        print_bonnetje_zakelijk(totaal)

    print(AFSLUITING)

main()