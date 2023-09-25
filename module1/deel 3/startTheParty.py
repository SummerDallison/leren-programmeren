gastheer = False
gasten = True
drank = True
chips = True

naam = input("Voer je naam in : ").lower()
naam == "summer" or "summer dallison"
naam != "wilfred" or "wilfred bouwman"

if (gasten and (chips and drank)) or (gastheer and drank or (gasten or chips)) or naam:
    print('Start the Party')
else:
    print('No Party')