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

SPIDERMAN_TEXT = {
    'intro' : [
        colored('Je wordt om 8 uur in de ochtend wakker in je bed op halloween.','blue'),
        colored('Welke outfit doe je vandaag aan?','blue')
    ],
    'prompt' : colored('Casual, Spider-Suit','blue'),
    'school' : [
        colored('Je hebt de outfit "{outfit}" gekozen!','blue'),
        colored('Je gaat naar school maar je bent 5 minuten te laat.','blue'),
        colored('Je gaat naar je eerste les, wiskunde...','blue'),
        colored('Eenmaal binnen gekomen zie je dat de docent al boos kijkt.','blue'),
        colored('Je bent te laat, MAAR als je deze vraag goed beantwoord dan mag je blijven.','yellow')
    ],
    'math' : colored('Wat is de wortel van "4 x (7:(15-10))?','yellow'),
    'correct' : [
        colored('Top gedaan 5.6 is helemaal goed!','green'),
        colored('Top of the class ending.','magenta')
    ],
    'incorrect' : [
        colored('Dat is helemaal fout, ga jij maar melden bij de directie.','yellow'),
        colored('Je bent op de gang onderweg naar de directie.','blue')
    ],
    'excuse' : colored('Alleen omdat ik maar 5 minuutjes te laat ben.','light_cyan'),
    'report_principal' : colored('Ga je melden bij directie?','blue'),
    'principal' : [
        colored('Waarom ben je eruit gestuurd?','yellow'),
        colored('Alleen omdat ik maar 5 minuutjes te laat ben.','light_cyan'),
        colored('Je bent gecatched door directie, laat je nooit vangen!','red')
    ],
    'run' : [
        colored('WAT JE GAAT NIET, IK WIST NIET DAT JE DIT IN JE HAD!','blue'),
        colored('RENNEN!!!!!','blue'),
        colored('Je rent heel hard door de gangen van de school!','blue'),
        colored('Achter je merk je dat je word achtervolgt door medewerkers.','blue'),
        colored('Je komt aan bij een lege gang, een open raam en een deur waarvan je niet weet waar het naartoe gaat.','blue')
    ],
    'hallway_prompt' : colored('Gang, Deur, Raam','blue'),
    'hallway' : [
        colored('Je rent de gang uit...','blue'),
        colored('Je ziet de uitgang aan het eind','blue'),
        colored('BOEM, ineens staat de concierge voor je en pakt je bij je kraag.','blue'),
        colored('Je bent gepakt door de concierge.','red')
    ],
    'door' : [
        colored('Je trekt de deur op en sluit hem direct achter.','blue'),
        colored('Na 3 seconden goed ademen, besef je dat je in een kast bent gestormt.','blue'),
        colored('Ineens trekt docent gym de deur van de kast open en trekt je de kast uit.','blue'),
        colored('Je bent gepakt door de gym docent en meegenomen naar het nablijf lokaal.','red'),
        colored('Voor de rest van de game moet je nablijven.','red')
    ],
    'window' : colored('Je springt door het raam.','blue'),
    'window_death' : [
        colored('Na een goeie seconden besef je je dat je je Web-Slingers niet hebt...','blue'),
        colored('Je viel dood op de grond','red')
    ],
    'window_escape' : [
        colored('Je pakt je Web-Slingers en slingert weg.','blue'),
        colored('Escape Ending','magenta')
    ]
}

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