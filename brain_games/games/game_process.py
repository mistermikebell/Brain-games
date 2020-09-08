# -*- coding:utf-8 -*-

"""Run one of games."""

import prompt

from brain_games.games import calc, even, gcd, progression


def module_choosing(game):
    if game == "even":
        return even.process()
    elif game == "gcd":
        return gcd.process()
    elif game == "progression":
        return progression.process()
    return calc.process()


def game(game):
    """Play a game."""
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {name}!\n'.format(name=name))
    for count in range(3):
        question, true_answer = module_choosing(game)
        print('Question: ', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != true_answer:
            return print("'{user_answer}' is wrong answer ;(.\
 Correct answer was '{true_answer}'.\nLet's try again,\
 {name}!".format(user_answer=user_answer, true_answer=true_answer, name=name))
            break
        if count == 2:
            print('Congratulations, {name}!'.format(name=name))
