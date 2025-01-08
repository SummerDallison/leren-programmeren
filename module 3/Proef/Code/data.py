BOLLETJE = 1.10
HOORNTJE = 1.25
BAKJE = 0.75
LITER_PRIJS = 9.80
BTW_PERCENTAGE = 9  # Zakelijke klanten betalen 9% BTW

TOPPING_PRIJZEN = {
    "geen": 0.0,
    "slagroom": 0.5,
    "sprinkels": 0.3,  # per bolletje
    "caramel saus": {"hoorntje": 0.6, "bakje": 0.9}
}

KEUZE_HOORNTJE_BAKJE = ['hoorntje', 'bakje']
KEUZE_SMAAK_BOLLETJE = ['aardbei', 'chocolade', 'munt', 'vanille']

PROMPT_WELKOM = "Welkom bij Papi Gelato"
PROMPT_KLANT = "Bent u 1) een particuliere klant of 2) een zakelijke klant? "
PROMPT_BOLLETJES = "Hoeveel bolletjes wilt u? "
PROMPT_LITERS = "Hoeveel liter wilt u? "
PROMPT_SMAAK = "Welke smaak wilt u voor bolletje nummer {bolletje_nummer}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? "
PROMPT_SMAAK_LITER = "Welke smaak wilt u voor liter nummer {liter_nummer}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? "
PROMPT_KEUZE = "Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? "
PROMPT_MEER = "Wilt u nog meer bestellen? (ja/nee) "
PROMPT_TOPPING = "Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? "

ANTWOORD_BAKJE = "Dan krijgt u van mij een bakje met {aantal} bolletjes."
ANTWOORD_HOORNTJE_BAKJE = "Hier is uw {keuze} met {aantal} bolletje(s)."
ANTWOORD_BAKJE_TOPPING = "Dan krijgt u van mij een bakje met {aantal} bolletjes en {topping}."
ANTWOORD_HOORNTJE_TOPPING = "Hier is uw {keuze} met {aantal} bolletje(s) en {topping}."
ANTWOORD_LITERS = "U heeft {aantal_liters} liter besteld."

ERROR_ONBEKEND = "Sorry, dat snap ik niet..."
ERROR_BAKKEN = "Sorry, zulke grote bakken hebben we niet."

BEGIN_BONNETJE = "\n---------- [Papi Gelato] ----------"
BON_SMAAK = "B. {smaak:13} {aantal} x €{BOLLETJE:.2f} = € {prijs:.2f}"
BON_HOORNTJES = "Hoorntje         {totaal_hoorntjes} x €{HOORNTJE:.2f} = € {prijs_hoorntjes:.2f}"
BON_BAKJES = "Bakje            {totaal_bakjes} x €{BAKJE:.2f} = € {prijs_bakjes:.2f}"
BON_TOPPING = "Topping                    = € {totaal_topping_prijs:.2f}"
BON_LITER = "L. {smaak:13} {aantal} x €{LITER_PRIJS:.2f} = € {liter_prijs:.2f}"
BON_OPTELTEKEN = "                         ---------- +"
BON_TOTAAL = "Totaal                     = € {totaal_prijs:.2f}"
BON_BTW = "BTW ({BTW_PERCENTAGE}%)                = € {btw_bedrag:.2f}"

AFSLUITING = "Bedankt en tot ziens!"