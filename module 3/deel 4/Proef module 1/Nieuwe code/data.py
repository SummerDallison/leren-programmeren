from termcolor import colored

TEST_ANSWERS = ['a','A','b','B','c','C']
YES_OPTIONS = ['y','j','yes','ja']
NO_OPTIONS = ['n','no','nee']
AVATAR_ANSWERS = ['Spider-Man','Steve','Joe','Thanos','Graig']

GAME_INTRO = {
    'intro' : [
    colored('Dag speler, dit is een adventure game waar het draait om keuzes.', 'blue'),
    colored('Om je bekend te maken met hoe dit spel werkt zal je nu een voorbeeld vraag krijgen.', 'blue'),
    colored('A, B of C?')
    ],
    'test_succes' : colored('Top! het gegeven antwoord is {test}.', 'green'),
    'test_failure' : colored('Helaas, dit was geen keuze. Probeer het opnieuw...','blue'),
    'avatar_promt' : [
        colored('Selecteer nu één van de volgende karakters.','blue'),
        colored('Spider-Man, Joe, Thanos, Graig','blue')
        ],
        'invalid_avatar' : colored('Je bent te dom om een karakter uit de lijst te kiezen, het spel stopt hier voor jou.', 'blue')
}


SPIDERMAN_TEXT = {
    'intro' : colored('Je wordt om 8 uur in de ochtend wakker in je bed op halloween.','blue'),
    'prompt' : [
    colored('Welke outfit doe je vandaag aan?','blue'),
    colored('Casual, Spider-Suit','blue')
    ],
    'classroom_interaction' : [
    colored('Je hebt de outfit "{outfit}" gekozen!','blue'),
    colored('Je gaat naar school maar je bent 5 minuten te laat.','blue'),
    colored('Je gaat naar je eerste les, wiskunde...','blue'),
    colored('Eenmaal binnen gekomen zie je dat de docent al boos kijkt.','blue'),
    colored('Je bent te laat, MAAR als je deze vraag goed beantwoord dan mag je blijven.','yellow'),
    colored('Wat is de wortel van "4 x (7:(15-10))?','yellow')
    ],
    'correct_answer' : [
    colored('Top gedaan 5.6 is helemaal goed!','green'),
    colored('Top of the class ending.','magenta')
    ],
    'wrong_answer' : [
    colored('Dat is helemaal fout, ga jij maar melden bij de directie.','yellow'),
    colored('Je bent op de gang onderweg naar de directie.','blue'),
    colored('Alleen omdat ik maar 5 minuutjes te laat ben.','light_cyan')
    ],
    'principal_prompt' : colored('Ga je melden bij directie?','blue'),
    'principal_office' : [
    colored('Waarom ben je eruit gestuurd?', 'yellow'),
    colored('Omdat ik 5 minuutjes te laat was...','light_cyan')
    ],
    'principal_ending' : colored('Je bent gecatched door directie, laat je nooit vangen!','red')
}


ESCAPE_SCENE = [
    colored('WAT JE GAAT NIET, IK WIST NIET DAT JE DIT IN JE HAD','blue'),
    colored('RENNEN!!!!!','blue'),
    colored('Je rent heel hard door de gangen van de school!','blue'),
    colored('Achter je merk je dat je word achtervolgt door medewerkers','blue'),
    colored('Je komt aan bij een lege gang, een open raam en een deur waarvan je niet weet waar het naartoe gaat.','blue'),
    colored('Gang, Deur, Raam','blue')
]

GAME_OVER = colored('Game-Over!', 'red')