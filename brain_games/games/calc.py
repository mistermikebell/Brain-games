# -*- coding:utf-8 -*-

"""Operations with numbers."""

from brain_games import game_logic

import random


def init_game():
    game_name = 'calc'
    description = 'What is the result of the expression?'
    game_logic.start(game_name, description)


def generate_task():
    signs = [' + ', ' - ', ' * ']
    number_1 = random.randint(0, 1000)
    number_2 = random.randint(0, 1000)
    choose_number = random.randint(0, len(signs) - 1)
    question = str(number_1) + signs[choose_number] + str(number_2)
    return question, str(eval(question))
