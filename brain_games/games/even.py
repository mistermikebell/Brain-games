# -*- coding:utf-8 -*-

"""Check if number is even."""

from brain_games import game_logic

import random


def init_game():
    game_name = 'even'
    description = 'Answer "yes" if number even otherwise answer "no".'
    game_logic.start(game_name, description)


def generate_task():
    number = random.randint(0, 1000)
    answer_options = ['yes', 'no']
    answer = answer_options[number % 2]
    return number, answer
