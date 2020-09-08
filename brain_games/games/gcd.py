# -*- coding:utf-8 -*-

"""Find GCD of two numbers."""

import random


def process():
    number_1 = random.randint(0, 1000)
    number_2 = random.randint(0, 1000)
    question = str(number_1) + ' ' + str(number_2)
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 %= number_2
        else:
            number_2 %= number_1
    gcd = number_1 + number_2
    return question, str(gcd)
