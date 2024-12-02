from data import *

def vraag_aantal_bolletjes():
    while True:
        try:
            aantal_bolletjes = int(input(PROMPT_BOLLETJES))
            if aantal_bolletjes < 1:
                print(ERROR_ONBEKEND)
            else:
                return aantal_bolletjes
        except ValueError:
            print(ERROR_ONBEKEND)

def vraag_hoorntje_of_bakje(aantal_bolletjes):
    while True:
        keuze = input(PROMPT_KEUZE.format(aantal=aantal_bolletjes)).lower()  # Vervang {aantal} met het werkelijke aantal
        if keuze in KEUZE_HOORNTJE_BAKJE:
            return keuze
        else:
            print(ERROR_ONBEKEND)

def geef_bakje_met_bolletjes(aantal_bolletjes):
    print(ANTWOORD_BAKJE.format(aantal=aantal_bolletjes))

def geef_order_bevestiging(keuze, aantal_bolletjes):
    print(ANTWOORD_HOORNTJE_BAKJE.format(keuze=keuze, aantal=aantal_bolletjes))

def vraag_meer_bestellen():
    while True:
        meer_bestellen = input(PROMPT_MEER).lower()
        if meer_bestellen == "ja":
            return True
        elif meer_bestellen == "nee":
            return False
        else:
            print(ERROR_ONBEKEND)
