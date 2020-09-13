# -*- coding:utf-8 -*-

"""Find missing number in a progression."""

from brain_games import game_logic

import random


def init_game():
    game_name = 'progression'
    description = 'What number is missing in the progression?'
    game_logic.start(game_name, description)


def generate_task():
    """Missing number in a progression function."""
    step = random.randint(1, 9)
    first_number = random.randint(1, 100)
    progression = [str(i) for i in range(first_number, 200, step)[:10]]
    place_number = random.randint(0, 9)
    answer = progression[place_number]
    progression[place_number] = ".."
    return " ".join(progression), answer
