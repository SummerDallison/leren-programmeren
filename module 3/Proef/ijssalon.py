def papi_gelato():
    print("Welkom bij Papi Gelato, je mag alle smaken kiezen zolang het maar vanille ijs is.")

    while True:
        # Stap 1: Vraag naar aantal bolletjes
        try:
            aantal_bolletjes = int(input("Hoeveel bolletjes wilt u?"))
        except ValueError:
            print("Sorry, dat snap ik niet...")
            continue

papi_gelato()