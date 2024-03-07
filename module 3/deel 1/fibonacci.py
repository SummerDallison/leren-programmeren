def fibonacci(aantal_getallen):
    fibonacci_reeks = [0, 1]

    for i in range(2, aantal_getallen):
        volgende_getal = fibonacci_reeks[-1] + fibonacci_reeks[-2]
        fibonacci_reeks.append(volgende_getal)

    return fibonacci_reeks

def bereken_gulden_snede(reeks):
    if len(reeks) >= 3:
        gulden_snede = reeks[-1] - reeks[-2]
        return gulden_snede
    
    else:
        return None

def bereken_fibonacci():
    aantal_getallen = int(input("Hoeveel getallen wil je berekenen in de fibonacci reeks? "))

    fib_reeks = fibonacci(aantal_getallen)

    print(f"Fibonacci reeks tot het {aantal_getallen} de getal: {fib_reeks}")

    gulden_snede = bereken_gulden_snede(fib_reeks)
    if gulden_snede is not None:
        print(f"Gulden snede op basis van de laatste twee getallen: {gulden_snede}")
    else:
        print("Niet genoeg getallen in de reeks om de gulden snede te berekenen.")

bereken_fibonacci()