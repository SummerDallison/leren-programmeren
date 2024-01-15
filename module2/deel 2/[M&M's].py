import random

mm_colors = ('oranje','groen','blauw','bruin')

while True:
    try:
        num_mms_to_add = int(input("Hoeveel M&M's moeten er aan de zak worden toegevoegd worden? "))
        break
    except ValueError:
        print("Voer alstublieft een getal in.")
  
mm_bag = []
for i in range(num_mms_to_add):
    random_color = random.choice(mm_colors)
    mm_bag.append(random_color)
            
print("Inhoud van de M&M-zak: ")
for color in mm_bag:
    print(color)