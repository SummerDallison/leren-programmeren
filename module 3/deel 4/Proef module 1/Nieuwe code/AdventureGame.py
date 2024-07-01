from functions import *
from data import *

def main():
    clear_and_print(colored(INTRO_TEXT, 'blue'))
    clear_and_print(colored(TUTORIAL_TEXT, 'blue'))

    test = get_valid_input(colored(CHOICE_PROMPT, 'blue'), TEST_ANSWERS)
    clear_and_print(colored(TEST_SUCCESS.format(test=test.capitalize()), 'green'))

    clear_and_print(colored(SELECT_AVATAR, 'blue'))
    clear_and_print(colored(CHARACTER_OPTIONS, 'blue'))
    avatar = input().strip().capitalize()

    if avatar == 'Spider-man':
        Spiderman_scenario()
    elif avatar == 'Joe':
        Joe_scenario
    elif avatar == 'Thanos':
        Thanos_scenario()
    elif avatar == 'Graig':
        Graig_scenario()
    else:
        game_over(TOO_DUMB)

main()