# -*- coding:utf-8 -*-

"""Run one of games."""

import importlib

import prompt


def play_game(game, name):
    """Play a game."""
    for count in range(3):
        question, true_answer = game.generate_task()
        print('Question: ', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != true_answer:
            return print("'{user_answer}' is wrong answer ;(.\
 Correct answer was '{true_answer}'.\nLet's try again,\
 {name}!".format(user_answer=user_answer, true_answer=true_answer, name=name))
            break
        if count == 2:
            print('Congratulations, {name}!'.format(name=name))


def start(game_name, description):
    print('Welcome to the Brain Games!', description)
    module = '.' + game_name
    game = importlib.import_module(module, 'brain_games.games')
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {name}!\n'.format(name=name))
    play_game(game, name)
