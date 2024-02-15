from fruitmand import fruitmand
from operator import itemgetter

fruitmandSorted = sorted(fruitmand, key=itemgetter('weight'), reverse=True) 

for fruit in fruitmandSorted:
    weight_in_kg = fruit['weight']/1000
    print(f"{fruit['name']}: {weight_in_kg} kg")