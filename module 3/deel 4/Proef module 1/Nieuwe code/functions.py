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
        if user_input in valid_options:
            return user_input
        clear_and_print(colored('Ongeldige invoer. Probeer opnieuw.', 'blue'))

def game_over(message):
    clear_and_print(colored(message, 'red'))
    clear_and_print(colored(GAME_OVER, 'red'))
    exit()

# ------------------------- Avatar Scenarios -------------------------

#Spider-man Scenario

def spiderman_scenario():
    clear_and_print(colored(SPIDER_MAN_WAKEUP, 'blue'))

    clear_and_print(colored(OUTFIT_CHOICE, 'blue'))