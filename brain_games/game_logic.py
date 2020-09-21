# -*- coding:utf-8 -*-

"""Run one of games."""

import prompt


def play(game, user_name, rounds):
    """Play a game."""
    for count in range(rounds):
        question, true_answer = game()
        print('Question: ', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != true_answer:
            print("'{mistake}' is wrong answer ;(.\
 Correct answer was '{answer}'.\nLet's try again,\
 {name}!".format(mistake=user_answer, answer=true_answer, name=user_name))
            break
        if count == rounds - 1:
            print('Congratulations, {name}!'.format(name=user_name))


def start(game, description, rounds=3):
    print('Welcome to the Brain Games!', description)
    user_name = prompt.string('\nMay I have your name? ')
    print('Hello, {}!\n'.format(user_name))
    play(game, user_name, rounds)
