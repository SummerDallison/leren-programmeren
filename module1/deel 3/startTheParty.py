gastheer_naam = input("Voer je naam in (Laat leeg als er geen gastheer is): ").lower()

gasten = int(input("Voer aantal gasten in : "))

drank = True
chips = True

mijn_naam = gastheer_naam == "summer" or gastheer_naam == "summer dallison"
lsb_docent_naam = gastheer_naam == "wilfred" or gastheer_naam == "wilfred bouwman"

if mijn_naam:
    print("Er is hoe dan ook een feest.")
elif lsb_docent_naam:
    print("Er is hoe dan ook geen feest.")
elif gasten < 4:
    print("Het feest kan pas beginnen wanneer er minimaal 4 gasten zijn.")
elif gasten > 20:
    print("Een feest kan niet starten wanneer er meer dan 20 gasten aanwezig zijn.")
elif (gasten and chips and drank) or (gastheer_naam and drank):
    print('Start the Party')
else:
    print('No Party')