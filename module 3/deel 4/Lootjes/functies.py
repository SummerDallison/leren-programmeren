import random

def input_yes_no(prompt):
    while True:
        antwoord = input(prompt + " (j/n): ").lower()
        if antwoord in ('j', 'n'):
            return antwoord == 'j'
        print("Ongeldige invoer. Voer alstublieft 'j' of 'n' in.")