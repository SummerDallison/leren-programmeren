from data import PROMPT_WELKOM, AFSLUITING
from functions import *

def start_programma():
    print(PROMPT_WELKOM)
    
    while True:
        aantal = vraag_bolletjes()

        if check_aantal_bolletjes(aantal):  
            keuze = vraag_keuze(aantal) 
            if keuze:
                pass 

        antwoord = vraag_meer_bestellen()
        
        if antwoord == 'nee':
            print(AFSLUITING)  
            break
        elif antwoord != 'ja':
            print(ERROR_ONBEKEND)  
            continue

start_programma()