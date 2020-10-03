# -*- coding:utf-8 -*-

"""Run one of games."""

import prompt


def play(generate_task, description):
    """Play a game."""
    ROUNDS_COUNT = 3
    print('Welcome to the Brain Games!')
    print(description)
    user_name = prompt.string('\nMay I have your name? ')
    print('Hello, {}!\n'.format(user_name))
    for count in range(ROUNDS_COUNT):
        question, true_answer = generate_task()
        print('Question: ', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != true_answer:
            print("'{user_answer}' is wrong answer ;(.\
 Correct answer was '{answer}'.\nLet's try again,\
 {name}!".format(user_answer=user_answer, answer=true_answer, name=user_name))
            return
    print('Congratulations, {name}!'.format(name=user_name))
