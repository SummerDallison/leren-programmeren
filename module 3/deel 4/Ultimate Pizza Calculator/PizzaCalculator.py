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

def bereken_totaalbedrag(aantal, prijs):
    return aantal * prijs

totaal_bedrag = totaal_bedrag_small + totaal_bedrag_medium + totaal_bedrag_large

print("Pizza bonnetje")
print("- - - - - - - - - - - - - - - - - - - ")
print(f"{aantal_small_pizza} Small Pizza's :   €{totaal_bedrag_small:.2f} ")
print(f"{aantal_medium_pizza} Medium Pizza's : €{totaal_bedrag_medium:.2f} ")
print(f"{aantal_large_pizza} Large Pizza's :   €{totaal_bedrag_large:.2f} ")
print("- - - - - - - - - - - - - - - - - - - ")
print(f"Totaal                             :   €{totaal_bedrag:.2f}")