antwoord1 = input("Is de kaas geel? (ja/nee) ").lower()

if antwoord1 == "ja":
    antwoord2 = input("Zitten er gaten in? (ja/nee) ").lower()
    if antwoord2 == "ja":
        antwoord3 = input("Is de kaas belachelijk duur? (ja/nee) ").lower()
        if antwoord3 == "ja":
            print("Het is de kaassoort: Emmenthaler.")
        else:
            print("Het is de kaassoort: Leerdammer.")
    else:
        antwoord4 = input("Is de kaas hard als steen (ja/nee) ").lower()
        if antwoord4 == "ja":
            print("Het is de kaassoort: Parmigiana Reggiano.")
        else:
            print("Het is de kaassoort: Goudse kaas.")
else:
    antwoord5 = input("Heeft de kaas blauwe schimmel? (ja/nee) ").lower()
    if antwoord5 == "ja":
        antwoord6 = input("Heeft de kaas korst? (ja/nee) ").lower()
        if antwoord6 == "ja":
            print("Het is de kaassoort: Blue de Rochbaron.")
        else:
            print("Het is de kaassoort: Foume d'ambert.")
    else:
        antwoord7 = input("Heeft de kaas korst? (ja/nee) ").lower()
        if antwoord7 == "ja":
            print("Het is de kaassoort: Camembert.")
        else:
            print("Het is de kaassoort: Mozzarella.")