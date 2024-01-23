PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

#bouw hieronder de flowchart na

while True:
    try:
        leeftijd = int(input("Wat is uw leeftijd? "))
        if leeftijd < 18:
            print("Sorry, u mag niet naar binnen.")
            print(f"Probeer het over {18-leeftijd} jaar nog eens.")
        elif leeftijd >= 18:
                input("Wat is uw naam? ")
        break

    except ValueError:
        print("Voer alstublieft uw leeftijd in.")