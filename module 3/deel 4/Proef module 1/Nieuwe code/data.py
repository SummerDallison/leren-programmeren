from termcolor import colored

TEST_ANSWERS = ['a','A','b','B','c','C']
AVATAR_ANSWERS = ['Batman','Spider-Man','Steve','Joe','Thanos','Graig']
CORRECT_AVATAR_ANSWER = 'Batman'

YES_OPTIONS = ['y','j','yes','ja']
NO_OPTIONS = ['n','no','nee']

INTRO_TEXT = {
    'intro' : [
        colored('Dag speler, dit is een adventure game waar het draait om keuzes.','blue'),
        colored('Om je bekend te maken met hoe dit spel werkt zal je nu een voorbeeld vraag krijgen.','blue')
    ],
    'prompt' : colored('A, B of C?','blue'),
    'correct' : colored('Top! het gegeven antwoord is {test}.','green'),
    'incorrect' : colored('Helaas, dit was geen keuze. Probeer het opnieuw...','blue'),
    'avatar' : [
        colored('Selecteer nu één van de volgende karakters.','blue'),
        colored('Spider-Man, Joe, Thanos, Graig','blue')
    ]
}

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
CLASS_ENDING = colored('Top of the class ending.','magenta')
WRONG_ANSWER = colored('Dat is helemaal fout, ga jij maar melden bij de directie.','yellow')
HEADING_TO_PRINCIPAL = colored('Je bent op de gang onderweg naar de directie.','blue')
LATE_EXCUSE = colored('Alleen omdat ik maar 5 minuutjes te laat ben.','light_cyan')
REPORT_TO_PRINCIPAL = colored('Ga je melden bij directie?','blue')
PRINCIPAL_QUESTION = colored('Waarom ben je eruit gestuurd?','yellow')
LATENESS_REASON = colored('Alleen omdat ik maar 5 minuutjes te laat ben.','light_cyan')
CAUGHT_BY_ADMINSTRATION = colored('Je bent gecatched door directie, laat je nooit vangen!','red')
SHOCKED_STATEMENT = colored('WAT JE GAAT NIET, IK WIST NIET DAT JE DIT IN JE HAD!','blue')
RUN_ALERT = colored('RENNEN!!!!!','blue')
RUNNING_THROUGH_SCHOOL = colored('Je rent heel hard door de gangen van de school!','blue')
CHASED_BY_STAFF = colored('Achter je merk je dat je word achtervolgt door medewerkers.','blue')
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
WEB_SLINGERS_ACTION = colored('Je pakt je Web-Slingers en slingert weg','blue')
ESCAPE_ENDING = colored('Escape Ending','magenta')

JOE_TEXT = [
    colored('Okay Joe-','blue'),
    colored('JOE MAMA, HAHHAHAHAH!!!','yellow'),
    colored('Wie ben jij dan weer?','blue'),
    colored('IK BEN DE RIZZLER, HAHAHAHAH!!!','yellow'),
    colored('Ja hier heb ik totaal geen zin in.','blue'),
    colored('Je spel is verpest door 9 jarige tiktok kinderen.','red')
]

THANOS_TEXT = [
    colored('Okay {avatar}, we gaan nu beginnen.','blue'),
    colored('Wacht eens even...','blue'),
    colored('Jij ging toch dood in "EndGame"?','blue'),
    colored('Wacht ik google het even...','blue'),
    colored('JA ZIE JE WEL, JE GING ZELFS TWEE KEER DOOD!','blue'),
    colored('{avatar} ging al dood in de film "Avengers: Endgame".','red')
]

GRAIG_TEXT = {
    'intro' : [
        colored('Hallo {avatar}, je bent een postbode.','blue'),
        colored('Laten we wat post posten!','blue'),
        colored('Je loopt door de wijken met HEEL VEEL post','blue')
    ],
    'prompt' : colored('Ga je post posten?','blue'),
    'success' : colored('Top! Je hebt post gebracht!','green'),
    'failure' : [
        colored('Je hebt niet genoeg post gebracht','red'),
        colored('Je bent ontslagen!','red')
    ]
}

GAME_OVER = colored('Game-Over!','red')