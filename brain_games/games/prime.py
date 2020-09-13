# -*- coding:utf-8 -*-

"""Check if number is prime."""

from brain_games import game_logic

import random


def init_game():
    game_name = 'prime'
    description = 'Answer "yes" if given number is prime.\
 Otherwise answer "no".'
    game_logic.start(game_name, description)


def generate_task():
    number = random.randint(0, 1000)
    if number == 2:
        return number, 'no'
    elif number % 2 == 0:
        return number, 'no'
    divider = 3
    while divider**2 <= number and number % divider != 0:
        divider += 2
    if divider**2 > number:
        return number, 'yes'
    return number, 'no'
