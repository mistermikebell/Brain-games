# -*- coding:utf-8 -*-

"""Find GCD of two numbers."""

from brain_games import game_logic

import random


def calculate_gcd(number_1, number_2):
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 %= number_2
        else:
            number_2 %= number_1
    return number_1 + number_2


def generate_gcd():
    LIMIT = 1000
    number_1 = random.randint(0, LIMIT)
    number_2 = random.randint(0, LIMIT)
    question = str(number_1) + ' ' + str(number_2)
    answer = str(calculate_gcd(number_1, number_2))
    return question, answer


def init_game():
    DESCRIPTION = 'Find the greatest common divisor of given numbers.'
    game_logic.start(generate_gcd, DESCRIPTION)
