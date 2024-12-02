from data import *

def krijg_aantal_bolletjes():
    while True:
        try:
            aantal_bolletjes = int(input(PROMPT_BOLLETJES))
            if aantal_bolletjes > 0:
                return aantal_bolletjes
            else:
                print(ERROR_ONBEKEND)
        except ValueError:
            print(ERROR_ONBEKEND)

def verwerk_aantal_bolletjes(aantal_bolletjes):
    if 1 <= aantal_bolletjes <= 3:
        return aantal_bolletjes  # Ga door naar stap 2
    elif 4 <= aantal_bolletjes <= 8:
        print(ANTWOORD_BAKJE.format(aantal=aantal_bolletjes))
        return None  # Sla stap 2 over
    else:
        print(ERROR_BAKKEN)
        return False  # Retourneer False zodat de vraag opnieuw gesteld wordt

def vraag_keuze(aantal):
    while True:
        keuze = input(PROMPT_KEUZE.format(aantal=aantal)).lower()
        if keuze in KEUZE_HOORNTJE_BAKJE:
            print(ANTWOORD_HOORNTJE_BAKJE.format(keuze=keuze, aantal=aantal))
            return
        else:
            print(ERROR_ONBEKEND)

def vraag_meer_bestellen():
    while True:
        meer = input(PROMPT_MEER).lower()
        if meer == "ja":
            return True
        elif meer == "nee":
            print(AFSLUITING)
            return False
        else:
            print(ERROR_ONBEKEND)