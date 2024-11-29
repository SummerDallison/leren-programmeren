from data import *

def vraag_aantal_bolletjes():
    try:
        aantal_bolletjes = int(input(PROMPT_BOLLETJES))
        return aantal_bolletjes
    except ValueError:
        print(ERROR_ONBEKEND)
        return None

def vraag_hoorntje_of_bakje(aantal_bolletjes):
    while True:
        keuze = input(PROMPT_KEUZE).lower()
        if keuze in KEUZE_HOORNTJE_BAKJE:
            return keuze
        else:
            print(ERROR_ONBEKEND)

def vraag_meer_bestellen():
    while True:
        meer_bestellen = input(PROMPT_MEER).lower()
        if meer_bestellen == "ja":
            return True
        elif meer_bestellen == "nee":
            return False
        else:
            print(ERROR_ONBEKEND)