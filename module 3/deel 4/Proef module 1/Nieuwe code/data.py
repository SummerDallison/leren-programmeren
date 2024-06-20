from termcolor import colored

TEST_ANSWERS = ['a','A','b','B','c','C']
AVATAR_ANSWERS = ['Batman','Spider-Man','Steve','Joe','Thanos','Graig']
CORRECT_AVATAR_ANSWER = 'Batman'

YES_OPTIONS = ['y','j','yes','ja']
NO_OPTIONS = ['n','no','nee']

#Introduction/Endings texts
INTRO_TEXT = colored('Dag speler, dit is een adventure game waar het draait om keuzes.','blue')
EXAMPLE_TEXT = colored('Om je bekend te maken met hoe dit spel werkt zal je nu een voorbeeld vraag krijgen.','blue')
CHOICE_PROMPT = colored('A, B of C?','blue')
WRONG_CHOICE = colored('Helaas, dit was geen keuze. Probeer het opnieuw...','blue')
CORRECT_CHOICE = colored('Top! het gegeven antwoord is {test}.','green')
AVATAR_PROMPT = colored('Selecteer nu één van de volgende karakters.','blue')
AVATAR_OPTIONS = colored('Spider-Man, Joe, Thanos, Graig','blue')
CLASS_ENDING = colored('Top of the class ending.','magenta')
GAME_OVER = colored('Game-Over!','red')

#Spider-Man Storyline texts
STARTING_SCENE = colored('Je wordt om 8 uur in de ochtend wakker in je bed op halloween.','blue')
OUTFIT_PROMPT = colored('Welke outfit doe je vandaag aan?','blue')
OUTFIT_OPTIONS = colored('Casual, Spider-Suit','blue')
CHOSEN_OUTFIT = colored('Je hebt de outfit "{outfit}" gekozen!','blue')
LATE_TO_SCHOOL = colored('Je gaat naar school maar je bent 5 minuten te laat.','blue')
ENTER_MATH_CLASS = colored('Je gaat naar je eerste les, wiskunde...','blue')
ANGRY_TEACHER_ENCOUNTER = colored('Eenmaal binnen gekomen zie je dat de docent al boos kijkt.','blue')
LATE_ARRIVAL_CONDITION = colored('Je bent te laat, MAAR als je deze vraag goed beantwoord dan mag je blijven.','yellow')
MATH_QUESTION = colored('Wat is de wortel van "4 x (7:(15-10))?','yellow')
CORRECT_ANSWER = colored('Top gedaan 5.6 is helemaal goed!','green')
WRONG_ANSWER = colored('Dat is helemaal fout, ga jij maar melden bij de directie.','yellow')
HEADING_TO_PRINCIPAL = colored('Je bent op de gang onderweg naar de directie.','blue')
LATE_EXCUSE = colored('Alleen omdat ik maar 5 minuutjes te laat ben.','light_cyan')
REPORT_TO_PRINCIPAL = colored('Ga je melden bij directie?','blue')
PRINCIPAL_QUESTION = colored('Waarom ben je eruit gestuurd?','yellow')
LATENESS_REASON = colored('Alleen omdat ik maar 5 minuutjes te laat ben.','light_cyan')
CAUGHT_BY_ADMINSTRATION = colored('Je bent gecatched door directie, laat je nooit vangen!','red')
SHOCKED_STATEMENT = colored('WAT JE GAAT NIET, IK WIST NIET DAT JE DIT IN JE HAD','blue')
RUN_ALERT = colored('RENNEN!!!!!','blue')
RUNNING_THROUGH_SCHOOL = colored('Je rent heel hard door de gangen van de school!','blue')
CHASED_BY_STAFF = colored('Achter je merk je dat je word achtervolgt door medewerkers','blue')
HALLWAY_CHOICE = colored('Je komt aan bij een lege gang, een open raam en een deur waarvan je niet weet waar het naartoe gaat.','blue')
HALLWAY_PROMPT = colored('Gang, Deur, Raam','blue')
EXIT_HALLWAY = colored('Je rent de gang uit...','blue')
EXIT_IN_SIGHT = colored('Je ziet de uitgang aan het eind','blue')
CONCIERGE_ENCOUNTER = colored('BOEM, ineens staat de concierge voor je en pakt je bij je kraag.','blue')
CAUGHT_BY_CONCIERGE = colored('Je bent gepakt door de concierge.','red')
EXIT_DOORWAY = colored('Je trekt de deur op en sluit hem direct achter.','blue')
REALIZATION_CLOSET_ENTRY = colored('Na 3 seconden goed ademen, besef je dat je in een kast bent gestormt.','blue')
GYM_TEACHER_ENCOUNTER = colored('Ineens trekt docent gym de deur van de kast open en trekt je de kast uit.','blue')
CAUGHT_BY_TEACHER = colored('Je bent gepakt door de gym docent en meegenomen naar het nablijf lokaal.','red')
DETENTION_ENDING = colored('Voor de rest van de game moet je nablijven.','red')
EXIT_WINDOW = colored('Je springt door het raam.','blue')
WEB_SLINGERS_FORGOTTEN = colored('Na een goeie seconden besef je je dat je je Web-Slingers niet hebt...','blue')
DEATH_ENDING = colored('Je viel dood op de grond','red')


'Waarom ben je eruit gestuurd?'
'Omdat ik 5 minuutjes te laat was...'
'Je bent gecatched door directie, laat je nooit vangen!'

'WAT JE GAAT NIET, IK WIST NIET DAT JE DIT IN JE HAD'
'RENNEN!!!!!'
'Je rent heel hard door de gangen van de school!'
'Achter je merk je dat je word achtervolgt door medewerkers'
'Je komt aan bij een lege gang, een open raam en een deur waarvan je niet weet waar het naartoe gaat.'
'Gang, Deur, Raam'

'Je rent de gang uit...'
'Je ziet de uitgang aan het eind'
'BOEM, ineens staat de concierge voor je en pakt je bij je kraag.'
'Je bent gepakt door de concierge.'

'Na 3 seconden goed ademen, besef je dat je in een kast bent gestormt.'
'Ineens trekt docent gym de deur van de kast open en trekt je de kast uit.'
'Je bent gepakt door de gym docent en meegenomen naar het nablijf lokaal.'
'Voor de rest van de game moet je nablijven.'

'Je springt door het raam.'
'Je pakt je Web-Slingers en slingert weg'
'Escape Ending'

'Dit is geen keuze, probeer het opnieuw'

'Okay Joe-'
'JOE MAMA, HAHHAHAHAH!!!'
'Wie ben jij dan weer?'
'IK BEN DE RIZZLER, HAHAHAHAH!!!'
'Ja hier heb ik totaal geen zin in.'
'Je spel is verpest door 9 jarige tiktok kinderen.'

'Okay {avatar}, we gaan nu beginnen.'
'Wacht eens even...'
'Jij ging toch dood in "EndGame"?'
'Wacht ik google het even...'
'JA ZIE JE WEL, JE GING ZELFS TWEE KEER DOOD!'
'{avatar} ging al dood in de film "Avengers: Endgame".'

'Hallo {avatar}, je bent een postbode.'
'Laten we wat post posten!'
'Je loopt door de wijken met HEEL VEEL post'
'Ga je post posten?'

'Top! Je hebt post gebracht!'
'Ga je post posten?'

'Je hebt niet genoeg post gebracht'
'Je bent ontslagen!'

'Op een manier kan je niet simpel ja of nee zeggen, het spel stopt hier voor jou.'

'Je bent te dom om een karakter uit de lijst te kiezen, het spel stopt hier voor jou.'