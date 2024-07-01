from functions import *
from data import *

def main():
    clear_and_print(colored(INTRO_TEXT, 'blue'))
    clear_and_print(colored(TUTORIAL_TEXT, 'blue'))

    test = get_valid_input(colored(CHOICE_PROMPT, 'blue'), TEST_ANSWERS)
    clear_and_print(colored(TEST_SUCCESS.format(test=test.capitalize()), 'green'))
   