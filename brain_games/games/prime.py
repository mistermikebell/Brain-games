# -*- coding:utf-8 -*-

"""Check if number is prime."""

import random


def process():
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
