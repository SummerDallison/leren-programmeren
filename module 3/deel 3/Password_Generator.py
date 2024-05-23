import random
import string

def generate_password():
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits_set = string.digits
    special_characters = '@#$%&_?'

    while True:
        num_uppercase = random.randint(2, 6)
        num_digits = random.randint(4, 7)
        num_specials = 3
        num_lowercase = 24 - num_uppercase - num_digits - num_specials

        uppercase = random.choices(uppercase_letters, k=num_uppercase)
        lowercase = random.choices(lowercase_letters, k=num_lowercase)
        specials = random.choices(special_characters, k=num_specials)
        digits = random.choices(digits_set, k=num_digits)

        combined_characters = uppercase + lowercase + specials + digits
        random.shuffle(combined_characters)

        password = ''.join(combined_characters)

        #Controleer of de 2 middelste posities een hoofdletter is, zo ja, begin opnieuw
        if any([password[11].isupper(), password[12].isupper()]):
            continue

        #Controleer of het laatste karakter een kleine letter is, zo ja, begin opnieuw
        if password[-1].islower():
            continue

        #Controleer of het eerste of laatste karakter een speciaal karakter is, zo ja, begin opnieuw
        if password[0] in special_characters or password[-1] in special_characters:
            continue

        #Controleer of een van de eerste drie karakters een cijfer is, zo ja, begin opnieuw
        if password[0].isdigit() or password[1].isdigit() or password[2].isdigit():
            continue

        return password

wachtwoord = generate_password()
print(wachtwoord)