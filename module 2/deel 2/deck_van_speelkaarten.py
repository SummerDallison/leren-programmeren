import random

suits = ['harten','klaveren','schoppen','ruiten']
ranks = ['2','3','4','5','6','7','8','9','10','boer','vrouw','heer','aas']
deck = ['joker','joker'] + [f'{suit} {rank}' for suit in suits for rank in ranks]

random.shuffle(deck)

for i in range(1,8):
    print(f"Kaart {i}: {deck.pop(0)}")

print(f"\nDeck ({len(deck)} kaarten): {deck}")