#Functie om de volgende reeks te maken
def generate_next_sequence(sequence):
    next_sequence = ""
    index = 0
    while index < len(sequence):
        count = 1
        #Kijk hoe vaak hetzelfde getal achter elkaar voorkomt
        while index + 1 < len(sequence) and sequence[index] == sequence[index + 1]:
            index += 1
            count += 1
        next_sequence += str(count) + sequence[index]
        index += 1
    return next_sequence

#Deze functie blijft de reeks printen totdat er twee 3'en achter elkaar staan
def find_sequence():
    current_sequence = "1" #Start met de eerste regel
    while "33" not in current_sequence:
        print(current_sequence)
        current_sequence = generate_next_sequence(current_sequence)
    print(current_sequence)

find_sequence()