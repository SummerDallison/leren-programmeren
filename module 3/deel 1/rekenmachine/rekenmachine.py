from functions import *

def calculator():
    n1 = False
    
    while True:
        if n1 is False:
            n1_input = input("Voer het eerste getal in: ")
            if not n1_input.replace('.','').replace('-','').isdigit():
                print("Ongeldige invoer. Voer alstublieft een getal in.")
                continue
            n1 = float(n1_input)
            
            while True:
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
                
                if choice.upper() in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                    break
                else:
                    print("Ongeldige invoer. Voer alstublieft 'A', 'B', 'C', 'D', 'E', 'F', 'G' of 'H' in.")

        else:
            while True:
                choice = input(f"Wil je wat met de uitkomst ({result}) doen?\n"
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
                
                if choice.upper() in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
                    break
                else:
                    print("Ongeldige invoer. Voer alstublieft 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' of 'I' in.")

        if choice.upper() == 'I':
            print(f"Uiteindelijke resultaat: {n1}")
            break

        if choice.upper() not in ['E', 'F', 'G', 'H', 'I']:
            while True:
                n2_input = input("Voer het tweede getal in: ")
                if not n2_input.replace(',','').replace('-','').isdigit():
                    print("Ongeldige invoer. Voer alstublieft een getal in.")
                    continue
                n2 = float(n2_input)
                break
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

calculator()