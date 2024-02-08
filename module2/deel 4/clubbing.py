PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

#bouw hieronder de flowchart na

while True:
    try:
        leeftijd = int(input("Wat is uw leeftijd? "))
        
        if leeftijd < 18:
            print("Sorry, u mag niet naar binnen.")
            print(f"Probeer het over {18 - leeftijd} jaar nog eens.")

        elif leeftijd >= 18:
                
            while True:
                naam = input("Wat is uw naam? ")

                if naam.isalpha():

                    bandje_stempel = []

                    if naam.lower() in VIP_LIST:

                        if leeftijd >= 21:
                            bandje_stempel.append("blauw bandje")
                            print(f"U krijgt van mij een {bandje_stempel[0]}.")

                        else:
                            bandje_stempel.append("rood bandje")
                            print(f"U krijgt van mij een {bandje_stempel[0]}.")
                    
                    else:

                        if leeftijd >= 21:
                            bandje_stempel.append("stempel")
                            print(f"U krijgt van mij een {bandje_stempel[0]}.")
                    
                    DRANKJES = input(f"Wat wilt u drinken? ")

                    if DRANKJES.lower() == "cola":
                        if "blauw bandje" in bandje_stempel or "rood bandje" in bandje_stempel:
                            print("Alstublieft, complimenten van het huis.")

                        else:
                            print(f"Alstublieft uw {DRANKJES.lower()}, dat is dan €{PRIJS_COLA:.2f}.")
                    
                    elif DRANKJES.lower() == "bier":
                        
                        if "blauw bandje" in bandje_stempel or "rood bandje" in bandje_stempel or "stempel" in bandje_stempel:
                            
                            if "blauw bandje" in bandje_stempel or "rood bandje" in bandje_stempel:
                                print("Alstublieft, complimenten van het huis.")
                            
                            else:
                                print(f"Alstublieft uw {DRANKJES.lower()}, dat is dan €{PRIJS_BIER:.2f}.")
                        
                        else:
                            print("Sorry, u mag geen alcohol bestellen onder de 21.")
                            print(f"Probeer het over {21 - leeftijd} jaar nog eens.")

                    elif DRANKJES.lower() == "champagne":

                        if "blauw bandje" in bandje_stempel or "rood bandje" in bandje_stempel:

                            if "blauw bandje" in bandje_stempel:
                                print(f"Alstublieft uw {DRANKJES.lower()}, dat is dan €{PRIJS_CHAMPAGNE:.2f}.")

                            else:
                                print("Sorry, u mag geen alcohol bestellen onder de 21.")
                                print(f"Probeer het over {21 - leeftijd} jaar nog eens.")
                        
                        else:
                            print("Sorry, alleen vips mogen champagne bestellen.")

                    else:
                        print("Sorry, geen idee wat u bedoelt, hier een glaasje water.")

                else:
                    print("Voer alstublieft uw naam in.")
                    continue
                break

        break

    except ValueError:
        print("Voer alstublieft uw leeftijd in.")