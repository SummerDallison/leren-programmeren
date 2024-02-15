from fruitmand import fruitmand

watermelon = {
    'name' : 'watermeloen',
    'weight' : 2500,
    'color' : 'green',
    'round' : True
}
fruitmand.append(watermelon)

totalWeight = 0

for fruit in fruitmand:
    totalWeight += fruit['weight']

print(totalWeight)