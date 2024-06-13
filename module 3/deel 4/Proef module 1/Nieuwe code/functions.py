import os
import time
from termcolor import colored
from data import *

def sprint(text, delay=0.065):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()