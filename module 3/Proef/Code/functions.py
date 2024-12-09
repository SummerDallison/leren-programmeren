from data import *

def vraag_aantal_bolletjes():
    while True:
        try:
            aantal_bolletjes = int(input(PROMPT_BOLLETJES))
            return aantal_bolletjes
        except ValueError:
            print(ERROR_ONBEKEND)

def vraag_smaak_bolletje(bolletje_nummer):
    while True:
        keuze_smaak = input(PROMPT_SMAAK.format(X=bolletje_nummer)).lower()
        if keuze_smaak == 'a':
            return 'aardbei'
        elif keuze_smaak == 'c':
            return 'chocolade'
        elif keuze_smaak == 'm':
            return 'munt'
        elif keuze_smaak == 'v':
            return 'vanille'
        else:
            print(ERROR_ONBEKEND)

def vraag_keuze_bakje_hoorntje(aantal_bolletjes):
    while True:
        keuze = input(PROMPT_KEUZE.format(aantal=aantal_bolletjes)).lower()
        if keuze in KEUZE_HOORNTJE_BAKJE:
            return keuze
        else:
            print(ERROR_ONBEKEND)

def antwoord_bolletjes(aantal_bolletjes):
    smaken_lijst = []  # Om de gekozen smaken op te slaan

    if 1 <= aantal_bolletjes <= 3:
        keuze = vraag_keuze_bakje_hoorntje(aantal_bolletjes)
        print(ANTWOORD_HOORNTJE_BAKJE.format(keuze=keuze, aantal=aantal_bolletjes))

        # Vraag per bolletje naar de smaak
        for i in range(1, aantal_bolletjes + 1):
            smaak = vraag_smaak_bolletje(i)
            smaken_lijst.append(smaak)
        
        return keuze, smaken_lijst
    elif 4 <= aantal_bolletjes <= 8:
        print(ANTWOORD_BAKJE.format(aantal=aantal_bolletjes))

        # Vraag per bolletje naar de smaak
        for i in range(1, aantal_bolletjes + 1):
            smaak = vraag_smaak_bolletje(i)
            smaken_lijst.append(smaak)

        return "bakje", smaken_lijst
    elif aantal_bolletjes > 8:
        print(ERROR_BAKKEN)
        return False, []  
    else:
        print(ERROR_ONBEKEND)
        return False, []

def vraag_meer_bestellen():
    while True:
        meer_bestellen = input(PROMPT_MEER).lower()
        if meer_bestellen == "ja":
            return True 
        elif meer_bestellen == "nee":
            print(AFSLUITING)
            return False
        else:
            print(ERROR_ONBEKEND)

def print_bonnetje(totaal_bolletjes, totaal_hoorntjes, totaal_bakjes, smaken):
    print(BEGIN_BONNETJE)

    prijs_bolletjes = totaal_bolletjes * BOLLETJE
    prijs_hoorntjes = totaal_hoorntjes * HOORNTJE
    prijs_bakjes = totaal_bakjes * BAKJE

    # Print de smaken van de bolletjes
    for smaak in smaken:
        print(BON_BOLLETJES(smaak=smaak, BOLLETJE=BOLLETJE))

    if totaal_hoorntjes > 0:
        print(BON_HOORNTJES.format(totaal_hoorntjes=totaal_hoorntjes, HOORNTJE=HOORNTJE, prijs_hoorntjes=prijs_hoorntjes))
    if totaal_bakjes > 0:
        print(BON_BAKJES.format(totaal_bakjes=totaal_bakjes, BAKJE=BAKJE, prijs_bakjes=prijs_bakjes))

    totaal_prijs = prijs_bolletjes + prijs_hoorntjes + prijs_bakjes
    print(BON_OPTELTEKEN)
    print(BON_TOTAAL.format(totaal_prijs=totaal_prijs))

    print(AFSLUITING)