import os, time
from time import sleep
from data import *

def sprint(text, delay=0.065):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls')

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        sprint('Ongeldige invoer. Probeer opnieuw.', 'blue')
        clear_screen()

def game_over(message):
    clear_screen()
    sprint(message)
    sleep(1)
    sprint(GAME_OVER)