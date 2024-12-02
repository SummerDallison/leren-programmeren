from data import *

def vraag_aantal_bolletjes():
    try:
        aantal_bolletjes = int(input(PROMPT_BOLLETJES))
        return aantal_bolletjes
    except ValueError:
        print(ERROR_ONBEKEND)
        return None


def vraag_bakje_of_hoorntje(aantal_bolletjes):
    keuze = input(PROMPT_KEUZE.format(aantal=aantal_bolletjes)).lower()
    if keuze in KEUZE_HOORNTJE_BAKJE:
        return keuze
    else:
        print(ERROR_ONBEKEND)
        return None


def is_valid_aantal_bolletjes(aantal_bolletjes):
    if aantal_bolletjes is None:
        return False
    if 1 <= aantal_bolletjes <= 3 or 4 <= aantal_bolletjes <= 8:
        return True
    return False


def is_valid_keuze(keuze):
    return keuze in KEUZE_HOORNTJE_BAKJE