# -*- coding:utf-8 -*-

"""Check if number is even."""

from brain_games import game_logic

import random


def generate_task():
    LIMIT = 1000
    question = random.randint(0, LIMIT)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def init_game():
    DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'
    game_logic.play(generate_task, DESCRIPTION)
