from bird_pkg import birddetails
from playsound import playsound

import random


def show_mode_menu():
    print("\n\t\t           Mode Menu")
    print("\t\t ---------------------------------")
    print("\t\t|  1. Play       |  2. Study      |")
    print("\t\t ---------------------------------")
    print("\t\t|  3. Scoreboard |  4. Exit       |")
    print("\t\t ---------------------------------\n")


class Mode:
    def __init__(self, level):
        self.level = level


def play_mode():
    print("play mode")


def learn_mode():
    print("learn mode")


def show_scores():
    print("show scores")


def exit_game():
    print("exit game")