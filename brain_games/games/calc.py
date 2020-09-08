# -*- coding:utf-8 -*-

"""Operations with numbers."""

import random


def process():
    signs = [' + ', ' - ', ' * ']
    number_1 = random.randint(0, 1000)
    number_2 = random.randint(0, 1000)
    choose_number = random.randint(0, 2)
    question = str(number_1) + signs[choose_number] + str(number_2)
    return question, str(eval(question))
