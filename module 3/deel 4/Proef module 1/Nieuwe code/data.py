from termcolor import colored

TEST_ANSWERS = ['a','b','c']
AVATAR_ANSWERS = ['Batman','Spider-Man','Steve','Joe','Thanos','Graig']
CORRECT_AVATAR_ANSWER = ['Batman']

YES_OPTIES = ['y','j','yes','ja']
NO_OPTIES = ['n','no','nee']

INTRO_TEXTS = [
    colored("Dag speler, dit is een adventure game waar het draait om keuzes.", 'blue'),
    colored("Om je bekend te maken met hoe dit spel werkt zal je nu een voorbeeld vraag krijgen.", 'blue'),
    colored("A, B of C?", 'blue')
               ]

TEST_SUCCESS_TEXT = colored("Top! het gegeven antwoord is {}.", 'green')
TEST_FAILURE_TEXT = colored("Helaas, dit was geen keuze. Probeer het opnieuw...", 'blue')

AVATAR_SELECTION_TEXT = colored("Selecteer nu één van de volgende karakters: ", 'blue')
AVATAR_PROMPT = colored("Spider-Man, Joe, Thanos, Graig", 'blue')