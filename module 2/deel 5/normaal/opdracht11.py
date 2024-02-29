from fruitmand import fruitmand

beschikbare_kleuren = set()

for fruit in fruitmand:
    beschikbare_kleuren.add(fruit['color'])

while True:
    gekozen_kleur = input("Kies een kleur uit de beschikbare kleuren van de fruitmand: ").lower()

    if gekozen_kleur in beschikbare_kleuren:
        break

    else:
        print(f"De kleur {gekozen_kleur} zit niet in de fruitmand.")

aantal_ronde = 0
for fruit in fruitmand:
    if fruit['color'] == gekozen_kleur and fruit['round']:
        aantal_ronde += 1

aantal_niet_ronde = 0
for fruit in fruitmand:
    if fruit['color'] == gekozen_kleur and not fruit['round']:
        aantal_niet_ronde += 1

verschil = aantal_ronde - aantal_niet_ronde

if verschil > 0:
    print(f"Er zijn {abs(verschil)} meer ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")

elif verschil < 0:
    print(f"Er zijn {abs(verschil)} minder ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")

else:
    print(f"Er zijn {aantal_ronde} ronde vruchten en {aantal_niet_ronde} niet ronde vruchten in de kleur {gekozen_kleur}")