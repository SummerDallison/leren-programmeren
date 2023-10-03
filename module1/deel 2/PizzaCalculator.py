#Summer Dallison, opdracht PizzaCalculator

#prijzen van de verschillende soorten pizza's
prijs_small_pizza = 6.99
prijs_medium_pizza = 11.99
prijs_large_pizza = 16.49

#de klant kan de aantal pizza's(small, medium en large) die hij/zij wilt
while True:
    try:
        aantal_small_pizza = int(input("Hoeveel small pizza's wilt u hebben? "))
        break
    except ValueError:
        print("Dit is geen geldig bedrag.")

while True:
    try:
        aantal_medium_pizza = int(input("Hoeveel medium pizza's wilt u hebben? "))
        break
    except ValueError:
        print("Dit is geen geldig bedrag.")

while True:
    try:
        aantal_large_pizza = int(input("Hoeveel large pizza's wilt u hebben? "))
        break
    except ValueError:
        print("Dit is geen geldig bedrag.")

#Hier wordt de totaal bedrag van de small pizza, medium pizza en large pizza apart berekent.
totaal_bedrag_small = aantal_small_pizza*prijs_small_pizza
totaal_bedrag_medium = aantal_medium_pizza*prijs_medium_pizza
totaal_bedrag_large = aantal_large_pizza*prijs_large_pizza

#Hier bereken je het totaal bedrag van de small, medium en large pizza"s bij elkaar.
totaal_bedrag = totaal_bedrag_small + totaal_bedrag_medium + totaal_bedrag_large

#Dit is de bonnetje
print("Pizza bonnetje")
print("- - - - - - - - - - - - - - - - - - - ")
print(f"{aantal_small_pizza} Small Pizza's :   €{totaal_bedrag_small:.2f} ")
print(f"{aantal_medium_pizza} Medium Pizza's : €{totaal_bedrag_medium:.2f} ")
print(f"{aantal_large_pizza} Large Pizza's :   €{totaal_bedrag_large:.2f} ")
print("- - - - - - - - - - - - - - - - - - - ")
print(f"Totaal                             :   €{totaal_bedrag:.2f}")