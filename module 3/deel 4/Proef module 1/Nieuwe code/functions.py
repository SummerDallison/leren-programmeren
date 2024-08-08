from termcolor import colored
import os, time
from time import sleep
from data import *

# ------------------------- Common Functions -------------------------

def sprint(text, delay=0.065):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_and_print(text, delay=1):
    os.system('cls')
    sprint(text)
    sleep(delay)

def get_valid_input(prompt, valid_options):
    while True:
        clear_and_print(prompt)
        user_input = input().strip().lower()

        clear_and_print(f"Debug: User input = '{user_input}'")
        clear_and_print(f"Debug: Valid options = {valid_options}")

        if user_input in valid_options:
            return user_input
        clear_and_print(colored(ONGELDIGE_INVOER, 'blue'))

def game_over(message):
    clear_and_print(colored(message, 'red'))
    clear_and_print(colored(GAME_OVER, 'red'))
    exit()

# ------------------------- Avatar Scenarios -------------------------

# **** Spider-Man Scenario ****

def math_question():
    clear_and_print(colored(LATE_QUESTION, 'yellow'))

    while True:
        try:
            clear_and_print(colored(MATH_QUESTION, 'yellow'))
            math = float(input().strip())

            if math == 5.6:
                clear_and_print(colored(CORRECT_ANSWER.format(math=math), 'green'))
                clear_and_print(colored(TOP_CLASS_ENDING, 'magenta'))
                exit()
            else:
                clear_and_print(colored(INCORRECT_ANSWER, 'yellow'))
                clear_and_print(colored(DIRECTOR_OFFICE, 'blue'))
                clear_and_print(colored(JUST_5_MINUTES, 'light_cyan'))
                handle_director()
                break
        except ValueError:
            clear_and_print(colored(ONGELDIGE_INVOER, 'blue'))

def handle_director():
    director = get_valid_input(colored(REPORT_TO_DIRECTOR, 'blue'), YES_NO_OPTIONS)

    if director in YES_OPTIONS:
        clear_and_print(colored(WHY_SUSPENDED, 'yellow'))
        clear_and_print(colored(JUST_LATE_REASON, 'light_cyan'))
        game_over(CAUGHT_BY_DIRECTOR)
    elif director in NO_OPTIONS:
        handle_escape()

def handle_escape():
    clear_and_print(colored(NOT_EXPECTED, 'blue'))
    clear_and_print(colored(RUNNING_AWAY, 'blue'))
    clear_and_print(colored(RUNNING_HALLWAYS, 'blue'))
    clear_and_print(colored(CHASED_BY_STAFF, 'blue'))
    clear_and_print(colored(THREE_OPTIONS, 'blue'))

    ways = get_valid_input(colored(HALLWAY_DOOR_WINDOW, 'blue'), WAYS_OPTIONS)

    if ways == 'gang': 
        clear_and_print(colored(RUNNING_HALL, 'blue'))
        clear_and_print(colored(SEES_EXIT, 'blue'))
        clear_and_print(colored(CAUGHT_BY_CUSTODIAN, 'blue'))
        game_over(CAUGHT_BY_CUSTODIAN_END)
    elif ways == 'deur':
        clear_and_print(colored(DOOR_CLOSED, 'blue'))
        clear_and_print(colored(IN_CLOSET, 'blue'))
        clear_and_print(colored(GOT_OUT_BY_GYM_TEACHER, 'blue'))
        clear_and_print(colored(CAUGHT_BY_GYM_TEACHER, 'red'))
        game_over(DETENTION_END)
    elif ways == 'raam':
        clear_and_print(colored(JUMPED_OUT_WINDOW, 'blue'))
        if current_outfit == 'spider-suit':
            clear_and_print(colored(USED_WEB_SLINGERS, 'blue'))
            clear_and_print(colored(ESCAPE_ENDING, 'magenta'))
        else:
            clear_and_print(colored(NO_WEB_SLINGERS, 'blue'))
            game_over(FELL_DEAD)

def start_class(outfit):
    clear_and_print(colored(CHOSEN_OUTFIT.format(outfit=outfit), 'blue'))
    clear_and_print(colored(LATE_FOR_SCHOOL, 'blue'))
    clear_and_print(colored(FIRST_CLASS, 'blue'))
    clear_and_print(colored(ANGRY_TEACHER, 'blue'))
    math_question()

def Spiderman_scenario():
    clear_and_print(colored(SPIDER_MAN_WAKEUP, 'blue'))

    clear_and_print(colored(OUTFIT_CHOICE, 'blue'))
    global current_outfit
    current_outfit = get_valid_input(colored(OUTFIT_OPTIONS, 'blue'), ['casual', 'spider-suit'])

    if current_outfit == 'casual':
        start_class('Casual')
    elif current_outfit == 'spider-suit':
        start_class('Spider-suit')

# **** Joe Scenario ****

def Joe_scenario():
    clear_and_print(colored(JOE_DIALOGUE_1, 'blue'))
    clear_and_print(colored(JOE_DIALOGUE_2, 'blue'))
    clear_and_print(colored(RIZZLER_DIALOGUE_1, 'blue'))
    clear_and_print(colored(RIZZLER_DIALOGUE_2, 'blue'))
    clear_and_print(colored(NOT_INTERESTED, 'blue'))
    game_over(GAME_SPOILED)

# **** Thanos Scenario ****

def Thanos_scenario(avatar):
    clear_and_print(colored(THANOS_START.format(avatar=avatar), 'blue'))
    clear_and_print(colored(WAIT_A_SECOND, 'blue'))
    clear_and_print(colored(DIED_IN_ENDGAME, 'blue'))
    clear_and_print(colored(GOOGLE_CHECK, 'blue'))
    clear_and_print(colored(DIED_TWICE, 'blue'))
    game_over(ALREADY_DIED.format(avatar=avatar))

# **** Graig Scenario ****

def Graig_scenario(avatar):
    clear_and_print(colored(POSTMAN_GREETING.format(avatar=avatar), 'blue'))
    clear_and_print(colored(POST_OFFICE_TASK, 'blue'))
    clear_and_print(colored(LOTS_OF_MAIL, 'blue'))

    while True:
        clear_and_print(colored(POST_POSTING, 'blue'))
        answer = input().strip().lower()
        
        if answer in YES_OPTIONS:
            clear_and_print(colored(POST_DELIVERED, 'green'))
        elif answer in NO_OPTIONS:
            clear_and_print(colored(NOT_ENOUGH_MAIL, 'red'))
            game_over(FIRED)
        else:
            game_over(NOT_SIMPLE_ANSWER)