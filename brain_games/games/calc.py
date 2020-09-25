# -*- coding:utf-8 -*-

"""Operations with numbers."""

from brain_games import game_logic

import random


def calculate(num_1, num_2, sign):
    if sign == " + ":
        return num_1 + num_2
    if sign == " - ":
        return num_1 - num_2
    if sign == " * ":
        return num_1 * num_2


def generate_task():
    LIMIT = 100
    number_1 = random.randint(0, LIMIT)
    number_2 = random.randint(0, LIMIT)
    calculation_sign = random.choice([' + ', ' - ', ' * '])
    question = str(number_1) + calculation_sign + str(number_2)
    answer = str(calculate(number_1, number_2, calculation_sign))
    return question, answer


def init_game():
    DESCRIPTION = 'What is the result of the expression?'
    game_logic.play(generate_task, DESCRIPTION)
