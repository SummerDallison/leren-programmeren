from fruitmand import fruitmand

for fruit in fruitmand:
    if fruit.get('name') == 'druif':
        fruitmand.remove(fruit)

kleuren = set()

for fruit in fruitmand:
    kleuren.add(fruit['color'])

for kleur in kleuren:
    print(kleur)