def generate_sequence():
    sequence = "1"
    while "33" not in sequence:
        new_sequence = ""
        count = 1
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i - 1]:
                count += 1
            else:
                new_sequence += str(count) + sequence[i - 1]
                count = 1
        new_sequence += str(count) + sequence[-1]
        sequence = new_sequence
        print(sequence)

generate_sequence()