PIZZA_PRIJZEN = {
    'small' : 6.99,
    'medium' : 11.99,
    'large' : 16.49
}

def vraag_aantal_pizzas(formaat):
    while True:
        try:
            aantal = int(input(f"Hoeveel {formaat} pizza's wilt u hebben? "))
            if aantal < 0:
                raise ValueError("Aantal pizza's kan geen negatief getal zijn. Probeer het opnieuw")
            return aantal
        except ValueError:
            print("Dit is geen geldig getal. Probeer het opnieuw.")

def bereken_totaalbedrag(pizza_aantallen):
    totaal_bedrag = 0
    for formaat, aantal in pizza_aantallen.items():
        totaal_bedrag += aantal * PIZZA_PRIJZEN[formaat]
    return totaal_bedrag

def print_bonnetje(pizza_aantallen, totaal_bedrag):
    print("\nPizza bonnetje")
    print("- - - - - - - - - - - - - - - - - - - ")
    for formaat, aantal in pizza_aantallen.items():
        print(f"{aantal} {formaat} pizza's   : €{aantal * PIZZA_PRIJZEN[formaat]:.2f}")
    print("- - - - - - - - - - - - - - - - - - - ")
    print(f"Totaal                : €{totaal_bedrag:.2f}")

def start_pizzacalculator():
    pizza_aantallen = {}
    for formaat in PIZZA_PRIJZEN:
        pizza_aantallen[formaat] = vraag_aantal_pizzas(formaat)
    totaal_bedrag = bereken_totaalbedrag(pizza_aantallen)
    print_bonnetje(pizza_aantallen, totaal_bedrag)

start_pizzacalculator()