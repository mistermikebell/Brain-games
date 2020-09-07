# -*- coding:utf-8 -*-

"""Check if number is odd."""

import random

import prompt


def odd_check(answer, number, name):
    """Check if number is odd."""
    if number % 2 == 0:
        if answer == 'yes':
            return 'Correct!'
        return "'{ans}' is wrong answer ;(. Correct answer was\
         'yes'.\nLet's try again, {name}!".format(ans=answer, name=name)
    if answer == 'no':
        return 'Correct!'
    return "'{ans}' is wrong answer ;(. Correct answer was\
         'no'.\nLet's try again, {name}!".format(ans=answer, name=name)


def game():
    """Play a game."""
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {name}!\n'.format(name=name))
    for count in range(3):
        number = random.randint(0, 1000)
        print('Question: ', number)
        answer = prompt.string('Your answer: ')
        output = odd_check(answer, number, name)
        if output != 'Correct!':
            print(output)
            break
        if count == 2:
            print('Congratulations, {name}!'.format(name=name))
