# -*- coding:utf-8 -*-

"""Check if number is prime."""

from brain_games import game_logic

import random


def isprime(num):
    if num == 2 or num % 2 == 0:
        return 'no'
    divider = 3
    while divider**2 <= num and num % divider != 0:
        divider += 2
    if divider**2 > num:
        return 'yes'
    return 'no'


def generate_prime():
    LIMIT = 1000
    question = random.randint(0, LIMIT)
    answer = isprime(question)
    return question, answer


def init_game():
    DESCRIPTION = 'Answer "yes" if given number is prime.\
 Otherwise answer "no".'
    game_logic.start(generate_prime, DESCRIPTION)
