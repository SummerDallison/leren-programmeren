BOLLETJE = 1.10
HOORNTJE = 1.25
BAKJE = 0.75

KEUZE_HOORNTJE_BAKJE = ['hoorntje', 'bakje']
KEUZE_SMAAK_BOLLETJE = ['aardbei', 'chocolade', 'munt', 'vanille']

PROMPT_WELKOM = "Welkom bij Papi Gelato"
PROMPT_BOLLETJES = "Hoeveel bolletjes wilt u? "
PROMPT_KEUZE = "Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? "
PROMPT_MEER = "Wilt u nog meer bestellen? (ja/nee) "
PROMPT_SMAAK = "Welke smaak wilt u voor bolletje nummer {X}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? "

ERROR_ONBEKEND = "Sorry, dat snap ik niet..."
ERROR_BAKKEN = "Sorry, zulke grote bakken hebben we niet."

ANTWOORD_BAKJE = "Dan krijgt u van mij een bakje met {aantal} bolletjes."
ANTWOORD_HOORNTJE_BAKJE = "Hier is uw {keuze} met {aantal} bolletje(s)."

BEGIN_BONNETJE = "\n--------- [Papi Gelato] ---------"
BON_SMAAK = "B. {smaak:13} {aantal} x €{BOLLETJE:.2f} = € {prijs:.2f}"
BON_HOORNTJES = "Hoorntjes       {totaal_hoorntjes} x €{HOORNTJE:.2f} = € {prijs_hoorntjes:.2f}"
BON_BAKJES = "Bakjes          {totaal_bakjes} x €{BAKJE:.2f} = € {prijs_bakjes:.2f}"
BON_OPTELTEKEN = "                        ---------- +"
BON_TOTAAL = "Totaal                   = € {totaal_prijs:.2f}"

AFSLUITING = "Bedankt en tot ziens!"