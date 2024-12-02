from data import *
from functions import *

def main():
    print(PROMPT_WELKOM)

    while True:
        # Vraag naar het aantal bolletjes
        aantal_bolletjes = vraag_aantal_bolletjes()

        # Verwerk het aantal bolletjes
        if not antwoord_bolletjes(aantal_bolletjes):
            continue

        # Vraag of ze meer willen bestellen
        if not vraag_meer_bestellen():
            break

if __name__ == "__main__":
    main()
