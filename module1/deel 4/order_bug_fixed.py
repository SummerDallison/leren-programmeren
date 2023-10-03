getal_1 = int(input("Voer eerste getal in : "))
getal_2 = int(input("Voer tweede getal in : "))

if getal_2 == 0:
    print("Kan niet delen door 0")
else:
    resultaat = getal_1/getal_2
    print (f"{getal_1} gedeeld door {getal_2} is gelijk aan {resultaat}")