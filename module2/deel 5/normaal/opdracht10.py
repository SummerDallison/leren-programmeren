from fruitmand import fruitmand
from operator import itemgetter

fruitmand_sorted = sorted(fruitmand, key=itemgetter('weight'), reverse=True) 

for fruit in fruitmand_sorted:
    gewicht_in_kg = fruit['weight']/1000
    print(f"{fruit['name']}: {gewicht_in_kg} kg")