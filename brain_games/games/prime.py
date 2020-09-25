# -*- coding:utf-8 -*-

"""Check if number is prime."""

from brain_games import game_logic

import random


def is_prime(num):
    if num == 2 or num % 2 == 0:
        return False
    divider = 3
    while divider**2 <= num and num % divider != 0:
        divider += 2
    if divider**2 > num:
        return True
    return False


def generate_task():
    LIMIT = 1000
    question = random.randint(0, LIMIT)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def init_game():
    DESCRIPTION = 'Answer "yes" if given number is prime.\
 Otherwise answer "no".'
    game_logic.play(generate_task, DESCRIPTION)
