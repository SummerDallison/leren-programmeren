from functions import *
from data import *

def main():
    print(PROMPT_WELKOM)

    while True:
        aantal_bolletjes = vraag_bolletjes()

        if aantal_bolletjes is not None:
            vraag_keuze(aantal_bolletjes)

        if not vraag_meer_bestellen():
            break

main()