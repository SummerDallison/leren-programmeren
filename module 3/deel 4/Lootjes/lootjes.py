from functies import * 

while len(deelnemers) < 3:
    voeg_deelnemer_toe(deelnemers, cadeau_wensen)

while input_yes_no("Wilt u meer deelnemers toevoegen?"):
    voeg_deelnemer_toe(deelnemers, cadeau_wensen)

print("De lootjes worden nu gecontroleerd en verdeeld.")
deelnemers_lootjes = verdelen_lootjes(deelnemers) 

for deelnemer, lootje in deelnemers_lootjes.items():
    print(f"{deelnemer} trekt lootje van {lootje}.")

while input_yes_no("Wilt u een lootje van een deelnemer opvragen?"):
    opvragen_lootje(deelnemers_lootjes, cadeau_wensen)
    break