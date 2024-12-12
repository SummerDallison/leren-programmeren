BOLLETJE = 1.10
HOORNTJE = 1.25
BAKJE = 0.75

KEUZE_HOORNTJE_BAKJE = ['hoorntje', 'bakje']
KEUZE_SMAAK_BOLLETJE = ['aardbei', 'chocolade', 'munt', 'vanille']

TOPPING_PRIJZEN = {
    "geen": 0.0,
    "slagroom": 0.50,
    "sprinkels": 0.30, # Per bolletje
    "caramel saus": {"hoorntje": 0.60, "bakje": 0.90}
}

PROMPT_WELKOM = "Welkom bij Papi Gelato, je mag alle smaken kiezen zolang het maar vanille ijs is."
PROMPT_BOLLETJES = "Hoeveel bolletjes wilt u? "
PROMPT_KEUZE = "Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? "
PROMPT_TOPPING = "Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? "
PROMPT_MEER = "Wilt u nog meer bestellen? (ja/nee) "
PROMPT_SMAAK = "Welke smaak wilt u voor bolletje nummer {X}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?"

ERROR_ONBEKEND = "Sorry, dat snap ik niet..."
ERROR_BAKKEN = "Sorry, zulke grote bakken hebben we niet."

ANTWOORD_BAKJE = "Dan krijgt u van mij een bakje met {aantal} bolletjes."
ANTWOORD_HOORNTJE_BAKJE = "Hier is uw {keuze} met {aantal} bolletje(s)."
ANTWOORD_BAKJE_TOPPING = "Dan krijgt u van mij een bakje met {aantal} bolletjes en met {topping}."
ANTWOORD_HOORNTJE_TOPPING = "Hier is uw {keuze} met {aantal} bolletje(s) en met {topping}."

BEGIN_BONNETJE = "\n--------- [Papi Gelato] ---------"
BON_BOLLETJES = "Bolletjes       {totaal_bolletjes} x €{BOLLETJE:.2f} = € {prijs_bolletjes:.2f}"
BON_HOORNTJES = "Hoorntjes       {totaal_hoorntjes} x €{HOORNTJE:.2f} = € {prijs_hoorntjes:.2f}"
BON_BAKJES = "Bakjes          {totaal_bakjes} x €{BAKJE:.2f} = € {prijs_bakjes:.2f}"
BON_TOPPINGS = "Topping                             = € {prijs_toppings:.2f}"
BON_OPTELTEKEN = "                        ---------- +"
BON_TOTAAL = "Totaal                   = € {totaal_prijs:.2f}"

AFSLUITING = "Bedankt en tot ziens!"