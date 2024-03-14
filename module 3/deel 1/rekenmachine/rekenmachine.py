from functions import *

def input_number(number):
    while True:
        num_input = input(number)
        if num_input.replace('.', '', 1).replace('-', '', 1).isdigit():
            return float(num_input)
        else:
            print("Ongeldige invoer. Voer alstublieft een geldig getal in.")

def calculator():
    n1 = input_number("Voer het eerste getal in: ")
    
    while True:
        if n1 is not False:
            choice = input(f"Wil je wat met de uitkomst ({n1}) doen?\n"
                           "A) iets optellen\n"
                           "B) iets aftrekken\n"
                           "C) met iets vermenigvuldigen\n"
                           "D) ergens door delen\n"
                           "E) ophogen\n"
                           "F) verlagen\n"
                           "G) verdubbelen\n"
                           "H) halveren\n"
                           "I) niets?\n"
                           "Kies een optie: ")
        else:
            choice = input("Wat wilt u doen?\n"
                           "A) getallen optellen\n"
                           "B) getallen aftrekken\n"
                           "C) getallen vermenigvuldigen\n"
                           "D) getallen delen\n"
                           "E) getal ophogen\n"
                           "F) getal verlagen\n"
                           "G) getal verdubbelen\n"
                           "H) getal halveren?\n"
                           "Kies een optie: ")
        
        if choice.upper() in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
            if choice.upper() != 'I':
                if choice.upper() not in ['E', 'F', 'G', 'H']:
                    n2 = input_number("Voer het tweede getal in: ")
                else:
                    if choice.upper() in ['E', 'F']:
                        n2 = 1
                    else:
                        n2 = 2
                
                if choice.upper() == 'A':
                    result = addition(n1, n2)
                    print(f"{n1} + {n2} = {result}")
                elif choice.upper() == 'B':
                    result = subtraction(n1, n2)
                    print(f"{n1} - {n2} = {result}")
                elif choice.upper() == 'C':
                    result = multiplication(n1, n2)
                    print(f"{n1} x {n2} = {result}")
                elif choice.upper() == 'D':
                    result = division(n1, n2)
                    print(f"{n1} : {n2} = {result}")
                elif choice.upper() == 'E':
                    result = addition(n1, 1)
                    print(f"{n1} + 1 = {result}")
                elif choice.upper() == 'F':
                    result = subtraction(n1, 1)
                    print(f"{n1} - 1 = {result}")
                elif choice.upper() == 'G':
                    result = multiplication(n1, 2)
                    print(f"{n1} x 2 = {result}")
                elif choice.upper() == 'H':
                    result = division(n1, 2)
                    print(f"{n1} : 2 = {result}")
                
                n1 = result
            else:
                print(f"Uiteindelijke resultaat: {n1}")
                break
        else:
            print("Ongeldige invoer. Voer alstublieft een geldige optie in.")

calculator()