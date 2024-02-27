from fruitmand import fruitmand

watermeloen = {
    'name' : 'watermeloen',
    'weight' : 2500,
    'color' : 'green',
    'round' : True
}
fruitmand.append(watermeloen)

totaalGewicht = 0

for fruit in fruitmand:
    totaalGewicht += fruit['weight']

print(totaalGewicht)