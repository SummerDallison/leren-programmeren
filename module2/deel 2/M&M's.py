import random

mm_colors = ('oranje','groen','blauw','bruin')

num_mms_to_add = int(input("Hoeveel M&M's moeten er aan de zak worden toegevoegd worden? "))

mm_bag = []
for i in range(num_mms_to_add):
    random_color = random.choice(mm_colors)
    mm_bag.append(random_color)

print("Inhoud van de M&M-zak: ")
for color in mm_bag:
    print(color)