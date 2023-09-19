aantal_croissantjes = 17
aantal_stokbroden = 2

prijs_per_croissant = 39
prijs_per_stokbrood = 278

aantal_kortingsbonnen = 3
waarde_per_kortingsbon = 50

totale_kosten = (aantal_croissantjes * prijs_per_croissant + aantal_stokbroden * prijs_per_stokbrood)/100

kortingsbonnen_waarde = aantal_kortingsbonnen * waarde_per_kortingsbon/100

te_betalen = totale_kosten - kortingsbonnen_waarde

print(f"Te betalen bedrag in euro: {te_betalen}")

print(f"De feestlunch kost je bij de bakker {te_betalen} euro voor de {aantal_croissantjes} croissantjes en de {aantal_stokbroden} stokbroden als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn!")