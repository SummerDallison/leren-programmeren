from fruitmand import fruitmand

for fruit in fruitmand:
    if fruit.get('name') == 'druif':
        fruitmand.remove(fruit)

colors = set()

for fruit in fruitmand:
    colors.add(fruit['color'])

for color in colors:
    print(color)