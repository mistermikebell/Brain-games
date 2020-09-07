# -*- coding:utf-8 -*-

"""Check if number is odd."""

import prompt, random


def odd_check(answer, number, name):
    if number % 2 == 0:
        if answer == 'yes':
            return 'Correct!'
        else:
            return "'{ans}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!".format(ans=answer, name=name)
    else:
        if answer == 'no':
            return 'Correct!'
        else:
            return "'{ans}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!".format(ans=answer, name=name)       


def game():
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {name}!\n'.format(name=name))
    for i in range(3):
        number = random.randint(0,1000)
        print('Question: ', number)
        answer = prompt.string('Your answer: ')
        result = odd_check(answer, number, name)
        if result != 'Correct!':
            print(result)
            break
        if i == 2:
            print('Congratulations, {name}!'.format(name=name))     	    
