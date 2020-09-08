# -*- coding:utf-8 -*-

"""Check if number is even."""

import random


def process():
    number = random.randint(0, 1000)
    if number % 2 == 0:
        return number, 'yes'
    return number, 'no'
