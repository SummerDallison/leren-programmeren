from termcolor import colored

TEST_ANSWERS = ['a','A','b','B','c','C']
YES_OPTIONS = ['y','j','yes','ja']
NO_OPTIONS = ['n','no','nee']
AVATAR_ANSWERS = ['Spider-Man','Steve','Joe','Thanos','Graig']

GAME_INTRO = [
    colored('Dag speler, dit is een adventure game waar het draait om keuzes.', 'blue'),
    colored('Om je bekend te maken met hoe dit spel werkt zal je nu een voorbeeld vraag krijgen.', 'blue'),
    colored('A, B of C?')
]
TEST_SUCCES = colored('Top! het gegeven antwoord is {test}.', 'green')
TEST_FAILURE = colored('Helaas, dit was geen keuze. Probeer het opnieuw...','blue')
AVATAR_PROMPT = [
    colored('Selecteer nu één van de volgende karakters.','blue'),
    colored('Spider-Man, Joe, Thanos, Graig','blue')
]
INVALID_AVATAR = colored('Je bent te dom om een karakter uit de lijst te kiezen, het spel stopt hier voor jou.', 'blue')

SPIDERMAN_INTRO = colored('Je wordt om 8 uur in de ochtend wakker in je bed op halloween.','blue')
SPIDERMAN_PROMPT = [
    colored('Welke outfit doe je vandaag aan?','blue'),
    colored('Casual, Spider-Suit','blue')
]
CLASSROOM_INTERACTION = [
    colored('Je hebt de outfit "{outfit}" gekozen!','blue'),
    colored('Je gaat naar school maar je bent 5 minuten te laat.','blue'),
    colored('Je gaat naar je eerste les, wiskunde...','blue'),
    colored('Eenmaal binnen gekomen zie je dat de docent al boos kijkt.','blue'),
    colored('Je bent te laat, MAAR als je deze vraag goed beantwoord dan mag je blijven.','yellow'),
    colored('Wat is de wortel van "4 x (7:(15-10))?','yellow')
]
CORRECT_ANSWER = [
    colored('Top gedaan 5.6 is helemaal goed!','green'),
    colored('Top of the class ending.','magenta')
]
WRONG_ANSWER = [
    colored('Dat is helemaal fout, ga jij maar melden bij de directie','yellow'),
    colored('Je bent op de gang onderweg naar de directie','blue'),
    colored('Alleen omdat ik maar 5 minuutjes te laat ben','light_cyan')
]
PRINCIPAL_PROMPT = colored('Ga je melden bij directie?','blue')

GAME_OVER = 'Game-Over!'