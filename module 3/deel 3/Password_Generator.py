import random
import string

password_length = 24

num_uppercase_letters = random.randint(2, 6)
uppercase_letters = random.sample(string.ascii_uppercase, num_uppercase_letters)

while True:
    middle_positions = [int(password_length / 2), int(password_length / 2) + 1]
    if all(letter not in middle_positions for letter in uppercase_letters):
        break
    else:
        uppercase_letters = random.sample(string.ascii_uppercase, num_uppercase_letters)

min_lowercase_letters = max(8, password_length - num_uppercase_letters)
lowercase_letters = random.sample(string.ascii_lowercase, min_lowercase_letters)