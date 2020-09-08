# -*- coding:utf-8 -*-

"""Find missing number in a progression."""

import random


def process():
    """Missing number in a progression function."""
    step = random.randint(1, 9)
    first_number = random.randint(1, 100)
    progression = [str(i) for i in range(first_number, 200, step)[:10]]
    place_number = random.randint(0, 9)
    answer = progression[place_number]
    progression[place_number] = ".."
    return " ".join(progression), answer
