gastheer_naam = input("Voer je naam in (Laat leeg als er geen gastheer is) : ").lower()

gasten = True
drank = True
chips = True

mijn_naam = gastheer_naam == "summer" or gastheer_naam == "summer dallison"
lsb_docent_naam = gastheer_naam != "wilfred" or gastheer_naam != "wilfred bouwman"

if mijn_naam:
    print("Er is hoe dan ook een feest.")
elif lsb_docent_naam:
    print("Er is hoe dan ook geen feest.")
elif(gasten and (chips and drank)) or (gastheer_naam and drank or (gasten or chips)):
    print('Start the Party')
else:
    print('No Party')