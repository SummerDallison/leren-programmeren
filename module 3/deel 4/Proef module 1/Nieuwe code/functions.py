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

def game_over(message):
    clear_screen()
    sprint(message)
    sleep(1)
    sprint(GAME_OVER)