from slowprint import sprint
from time import sleep
import os
from termcolor import colored

# red = fail ending
# blue = narrator
# green = good
# magenta = ending
# yellow = different person
# cyan = you

TEST_ANTWOORD = ['a','A','b','B','c','C']
AVATAR_ANTWOORD = ['Batman', 'Spider-Man', 'Steve', 'Joe', 'Thanos', 'Graig']
AVATAR_ANTWOORD_GOED = 'Batman'
YES = ['y','j','yes','ja']
NO = ['n','no','nee']

os.system('cls')
sprint(colored('Dag speler, dit is een adventure game waar het draait om keuzes.', 'blue'))
sleep(1)
os.system('cls')
sprint(colored('Om je bekend te maken met hoe dit spel werkt zal je nu een voorbeeld vraag krijgen.', 'blue'))
sleep(1)
os.system('cls')
sprint(colored('A, B of C?','blue'))
test = input()
while True:
    if test in TEST_ANTWOORD:
        os.system('cls')
        sprint(colored(f'Top! het gegeven antwoord is {test}.', 'green'))
        break
    else:
        os.system('cls')
        sprint(colored('Helaas, dit was geen keuze. Probeer het opnieuw...','blue'))
        sleep(1)
        os.system('cls')
        sprint(colored('A, B of C?','blue'))
        test = input()
sleep(1)
os.system('cls')
sprint(colored('Selecteer nu één van de volgende karakters.','blue'))
sleep(1)
os.system('cls')
sprint(colored('Spider-Man, Joe, Thanos, Graig','blue'))
avatar = input()
if avatar == 'Spider-Man':
    os.system('cls')
    sprint(colored('Je wordt om 8 uur in de ochtend wakker in je bed op halloween..','blue'))
    sleep(1)
    os.system('cls')
    sprint(colored('Welke outfit doe je vandaag aan?','blue'))
    sleep(1)
    os.system('cls')
    sprint(colored('Casual, Spider-Suit','blue'))
    outfit = input()
    os.system('cls')
    while True:
        if outfit == 'Casual':
            sprint(colored(f'Je hebt de outfit "{outfit}" gekozen!','blue'))
            sleep(1)
            os.system('cls')
            sprint(colored('Je gaat naar school maar je bent 5 minuten te laat.','blue'))
            sleep(1)
            os.system('cls')
            sprint(colored('Je gaat naar je eerste les, wiskunde...','blue'))
            sleep(1)
            os.system('cls')
            sprint(colored('Eenmaal binnen gekomen zie je dat de docent al boos kijkt.','blue'))
            sleep(1)
            os.system('cls')
            sprint(colored('Je bent te laat, MAAR als je deze vraag goed beantwoord dan mag je blijven.','yellow'))
            sleep(1)
            os.system('cls')
            sprint(colored('Wat is de wortel van "4 x (7:(15-10))"?','yellow'))
            math = input()
            os.system('cls')
            if math == '5.6':
                sprint(colored('Top gedaan 5.6 is helemaal goed!','green'))
                sleep(1)
                os.system('cls')
                sprint(colored('Top of the class ending.','magenta'))
                break
            else:
                sprint(colored('Dat is helemaal fout, ga jij maar melden bij de directie','yellow'))
                sleep(1)
                os.system('cls')
                sprint(colored('Je bent op de gang onderweg naar de directie','blue'))
                sleep(1)
                os.system('cls')
                sprint(colored('Alleen omdat ik maar 5 minuutjes te laat ben','light_cyan'))
                sleep(1)
                os.system('cls')
                sprint(colored('Ga je meldeen bij directie?','blue'))
                directie = input()
                os.system('cls')
                if directie in YES:
                    sprint(colored('Waarom ben je eruit gestuurd?','yellow'))
                    sleep(1)
                    os.system('cls')
                    sprint(colored('Omdat ik 5 minuutjes te laat was...','light_cyan'))
                    sleep(1)
                    os.system('cls')
                    sprint(colored('Je bent gecatched door directie, laat je nooit vangen!','red'))
                elif directie in NO:
                    sprint(colored('WAT JE GAAT NIET, IK WIST NIET DAT JE DIT IN JE HAD','blue'))
                    sleep(1)
                    os.system('cls')
                    sprint(colored('RENNEN!!!!!','blue'))
                    sleep(1)
                    os.system('cls')
                    sprint(colored('Je rent heel hard door de gangen van de school!','blue'))
                    sleep(1)
                    os.system('cls')
                    sprint(colored('Achter je merk je dat je word achtervolgt door medewerkers','blue'))
                    sleep(1)
                    os.system('cls')
                    sprint(colored('Je komt aan bij een lege gang, een open raam en een deur waarvan je niet weet waar het naartoe gaat.','blue'))
                    sleep(1)
                    os.system('cls')
                    sprint(colored('Gang, Deur, Raam','blue'))
                    ways = input()
                    os.system('cls')
                    if ways == 'Gang':
                        sprint(colored('Je rent de gang uit...','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Je ziet de uitgang aan het eind','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('BOEM, ineens staat de concierge voor je en pakt je bij je kraag.','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Je bent gepakt door de concierge.','red'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Game-Over!','red'))
                    elif ways == 'Deur':
                        sprint(colored('Je trekt de deur op en sluit hem direct achter.','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Na 3 seconden goed ademen, besef je dat je in een kast bent gestormt.','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Ineens trekt docent gym de deur van de kast open en trekt je de kast uit.','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Je bent gepakt door de gym docent en meegenomen naar het nablijf lokaal.','red'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Voor de rest van de game moet je nablijven.','red'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Game-Over!','red'))
                    elif ways == 'Raam':
                        sprint(colored('Je springt door het raam.','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Na een goeie seconden besef je je dat je je Web-Slingers niet hebt...','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Je viel dood op de grond','red'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Game-Over','red'))
            break
        elif outfit == 'Spider-Suit':
            sprint(colored(f'Je hebt de outfit "{outfit}" gekozen!','blue'))
            sleep(1)
            os.system('cls')
            sprint(colored('Je gaat naar school maar je bent 5 minuten te laat.','blue'))
            sleep(1)
            os.system('cls')
            sprint(colored('Je gaat naar je eerste les, wiskunde...','blue'))
            sleep(1)
            os.system('cls')
            sprint(colored('Eenmaal binnen gekomen zie je dat de docent al boos kijkt.','blue'))
            sleep(1)
            os.system('cls')
            sprint(colored('Je bent te laat, MAAR als je deze vraag goed beantwoord dan mag je blijven.','yellow'))
            sleep(1)
            os.system('cls')
            sprint(colored('Wat is de wortel van "4 x (7:(15-10))"?','yellow'))
            math = input()
            os.system('cls')
            if math == '5.6':
                sprint(colored('Top gedaan 5.6 is helemaal goed!','green'))
                sleep(1)
                os.system('cls')
                sprint(colored('Top of the class ending.','magenta'))
                break
            else:
                sprint(colored('Dat is helemaal fout, ga jij maar melden bij de directie','yellow'))
                sleep(1)
                os.system('cls')
                sprint(colored('Je bent op de gang onderweg naar de directie','blue'))
                sleep(1)
                os.system('cls')
                sprint(colored('Alleen omdat ik maar 5 minuutjes te laat ben','light_cyan'))
                sleep(1)
                os.system('cls')
                sprint(colored('Ga je meldeen bij directie?','blue'))
                directie = input()
                os.system('cls')
                if directie in YES:
                    sprint(colored('Waarom ben je eruit gestuurd?','yellow'))
                    sleep(1)
                    os.system('cls')
                    sprint(colored('Omdat ik 5 minuutjes te laat was...','light_cyan'))
                    sleep(1)
                    os.system('cls')
                    sprint(colored('Je bent gecatched door directie, laat je nooit vangen!','red'))
                elif directie in NO:
                    sprint(colored('WAT JE GAAT NIET, IK WIST NIET DAT JE DIT IN JE HAD','blue'))
                    sleep(1)
                    os.system('cls')
                    sprint(colored('RENNEN!!!!!','blue'))
                    sleep(1)
                    os.system('cls')
                    sprint(colored('Je rent heel hard door de gangen van de school!','blue'))
                    sleep(1)
                    os.system('cls')
                    sprint(colored('Achter je merk je dat je word achtervolgt door medewerkers','blue'))
                    sleep(1)
                    os.system('cls')
                    sprint(colored('Je komt aan bij een lege gang, een open raam en een deur waarvan je niet weet waar het naartoe gaat.'))
                    sleep(1)
                    os.system('cls')
                    sprint(colored('Gang, Deur, Raam','blue'))
                    ways = input()
                    os.system('cls')
                    if ways == 'Gang':
                        sprint(colored('Je rent de gang uit...','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Je ziet de uitgang aan het eind','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('BOEM, ineens staat de concierge voor je en pakt je bij je kraag.','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Je bent gepakt door de concierge.','red'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Game-Over!','red'))
                    elif ways == 'Deur':
                        sprint(colored('Je trekt de deur op en sluit hem direct achter.','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Na 3 seconden goed ademen, besef je dat je in een kast bent gestormt.','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Ineens trekt docent gym de deur van de kast open en trekt je de kast uit.','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Je bent gepakt door de gym docent en meegenomen naar het nablijf lokaal.','red'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Voor de rest van de game moet je nablijven.','red'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Game-Over!','red'))
                    elif ways == 'Raam':
                        sprint(colored('Je springt door het raam.','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Je pakt je Web-Slingers en slingert weg','blue'))
                        sleep(1)
                        os.system('cls')
                        sprint(colored('Escape Ending','magenta'))
            break
        else:
            sprint(colored('Dit is geen keuze, probeer het opnieuw','blue'))
elif avatar == 'Joe':
    os.system('cls')
    sprint(colored('Okay Joe-','blue'))
    os.system('cls')
    sprint(colored('JOE MAMA, HAHHAHAHAH!!!','yellow'))
    sleep(1)
    os.system('cls')
    sprint(colored('Wie ben jij dan weer?','blue'))
    sleep(0.8)
    os.system('cls')
    sprint(colored('IK BEN DE RIZZLER, HAHAHAHAH!!!','yellow'))
    sleep(1)
    os.system('cls')
    sprint(colored('Ja hier heb ik totaal geen zin in.','blue'))
    sleep(1)
    os.system('cls')
    sprint(colored('Je spel is verpest door 9 jarige tiktok kinderen.','red'))
    sleep(1)
    os.system('cls')
    sprint(colored('Game-Over!','red'))
elif avatar == 'Thanos':
    os.system('cls')
    sprint(colored(f'Okay {avatar}, we gaan nu beginnen.','blue'))
    sleep(1)
    os.system('cls')
    sprint(colored('Wacht eens even...','blue'))
    sleep(1)
    os.system('cls')
    sprint(colored('Jij ging toch dood in "EndGame"?','blue'))
    sleep(1)
    os.system('cls')
    sprint(colored('Wacht ik google het even...','blue'))
    sleep(1)
    os.system('cls')
    sprint(colored('JA ZIE JE WEL, JE GING ZELFS TWEE KEER DOOD!','blue'))
    sleep(1)
    os.system('cls')
    sprint(colored(f'{avatar} ging al dood in de film "Avengers: Endgame".','red'))
    sleep(1)
    os.system('cls')
    sprint(colored('Game-Over!','red'))
elif avatar == 'Graig':
    os.system('cls')
    sprint(colored(f'Hallo {avatar}, je bent een postbode.','blue'))
    sleep(1)
    os.system('cls')
    sprint(colored('Laten we wat post posten!','blue'))
    sleep(1)
    os.system('cls')
    sprint(colored('Je loopt door de wijken met HEEL VEEL post','blue'))
    sleep(1)
    os.system('cls')
    sprint(colored('Ga je post posten?','blue'))
    mail = input()
    while True:
        if mail in YES:
            os.system('cls')
            sprint(colored('Top! Je hebt post gebracht!','green'))
            sleep(1)
            os.system('cls')
            sprint(colored('Ga je post posten?','blue'))
            mail = input()
        elif mail in NO:
            os.system('cls')
            sprint(colored('Je hebt niet genoeg post gebracht','red'))
            sleep(1)
            os.system('cls')
            sprint(colored('Je bent ontslagen!','red'))
            sleep(1)
            os.system('cls')
            sprint(colored('Game-Over!','red'))
            break
        else:
            os.system('cls')
            sprint(colored('Op een manier kan je niet simpel ja of nee zeggen, het spel stopt hier voor jou.','blue'))
            sleep(1)
            os.system('cls')
            sprint(colored('Game-Over!','red'))
            break
else:
    os.system('cls')
    sprint(colored('Je bent te dom om een karakter uit de lijst te kiezen, het spel stopt hier voor jou.', 'blue'))
    sleep(1)
    os.system('cls')
    sprint(colored('Game-Over!','red'))